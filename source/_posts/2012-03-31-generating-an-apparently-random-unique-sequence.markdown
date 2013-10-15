---
layout: post
title: "Generating an Apparently Random Unique Sequence"
date: 2012-03-31 15:40
comments: true
github_issue_id: 5
categories: 
---

Using a sequentially increasing counter to generate an id token is easy.
Database sequences and auto-number columns make it fairly trivial to
implement. If that isn't available a simple file or shared memory counter can
be implemented in minutes. Displaying such a number to a client however may
give them more information than you would really like them to have about the
number of ids you are allocating per unit time. We'd really like  to obfuscate
the id somehow while retaining the uniqueness of the original sequence.

One way to do this is to use a combination of multiplication and modulo
arithmetic to map the sequence number into a constrained set. With careful
choice of the multiplicative constant and the modulo value the resulting
number can be made to wander rather effectively over the entire space of the
target set.

<!-- more -->

The basic math looks like this:  `f(n) := (n * p) % q`

- n := input sequence value
- p := step size
- q := maximum result size

`p` and `q` must be chosen such that:
- p < q
- p * q < arithmetic limit (2^31, 2^32, 2^63, 2^64, ... depending on the precision of the underlying system)
- p ⊥ q ([coprime](https://en.wikipedia.org/wiki/Coprime) or relatively prime)

With `p := 5` and `q := 12` our function will generate this output:  
<table class="border padded">
  <tr><th>n</th><td>1 </td><td> 2 </td><td> 3 </td><td> 4 </td><td> 5 </td><td> 6 </td><td> 7 </td><td> 8 </td><td> 9 </td><td> 10 </td><td> 11 </td></tr>
  <tr><th>f(n)</th><td>5 </td><td> 10 </td><td> 3 </td><td> 8 </td><td> 1 </td><td> 6 </td><td> 11 </td><td> 4 </td><td> 9 </td><td> 2 </td><td> 7 </td></tr>
</table>


Change `p` to 7 and you'll get:  
<table class="border padded">
  <tr><th>n</th><td>1 </td><td> 2 </td><td> 3 </td><td> 4 </td><td> 5 </td><td> 6 </td><td> 7 </td><td> 8 </td><td> 9 </td><td> 10 </td><td> 11 </td></tr>
  <tr><th>f(n)</th><td>7</td><td> 2</td><td> 9</td><td> 4</td><td> 11</td><td> 6</td><td> 1</td><td> 8</td><td> 3</td><td> 10</td><td> 5</td></tr>
</table>

The rational for keeping `p * q < limit` is that as `n` approaches `q` the
initial multiplication will approach `p * q` and if this calculation overflows
the available precision the result will wrap back into a previously traversed
space causing duplication. The same sort of thing will occur if `p` and `q`
are not coprime. The result of the modulo will exhibit a period equivalent to
the GCD of `p` and `q` rather than mapping the entire range of `q`
evenly.

Careful choice of `p` and `q` are key to getting a good spread in the output
of the function and maintaining the uniqueness of the result. One easy way to
ensure that the chosen coefficients are coprime is to make them both be prime
powers of prime numbers (eg 9^17, 13^11, 13^15, 19^7, ...).

This method is a type of [Linear congruential generator](https://en.wikipedia.org/wiki/Linear_congruential_generator) almost exactly equivalent to the [Park–Miller random number generator](https://en.wikipedia.org/wiki/Park%E2%80%93Miller_RNG).

Examples
--------

{% codeblock PHP lang:php %}
<?php
/**
 * Obfuscate an id generated from a linear sequence.
 *
 * @param int $n Input value
 * @param int $p Random walk step size
 * @param int $q Maximum result value
 * @return int Obfuscated result
 */
function obfuscate_id ($n, $p, $q) {
  return ($n * $p) % $q;
}
{% endcodeblock %}

{% codeblock PL/SQL lang:sql %}
FUNCTION obfuscate_id (n NUMBER, p NUMBER, q NUMBER) RETURN NUMBER IS
BEGIN
  RETURN MOD(n * p, q);
END f;
{% endcodeblock %}

----
Thanks to [Tim](http://www.timbarber.org/) for explaining all of this to me several times without becoming annoyed at the parts I wasn't getting.

*[GCD]: Greatest Common Divisor
