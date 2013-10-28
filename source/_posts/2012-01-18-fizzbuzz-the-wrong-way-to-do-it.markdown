---
layout: post
title: "FizzBuzz &mdash; the wrong way to do it"
date: 2012-01-18 21:47
comments: true
categories: algorithms
---
> Write a program that prints the numbers from 1 to 100. But for multiples of
> three print "Fizz" instead of the number and for the multiples of five print
> "Buzz". For numbers which are multiples of both three and five print
> "FizzBuzz".
> <small><a href="http://imranontech.com/2007/01/24/using-fizzbuzz-to-find-developers-who-grok-coding/">imranontech [at] googlemail.com</a></small>

<!-- more -->

{% codeblock fizzbuzz.py %}
#!/usr/bin/env python
for i in xrange(1, 101):
  print (not i % 3) * "Fizz" + (not i % 5) * "Buzz" or i
{% endcodeblock %}

{% codeblock fizzbuzz.php %}
<?php
$p = "printf"; $r = "str_repeat";
for ($i = 1; $i <= 100; $i++) {
  $p("%s\n", $r($i, $p("%s%s",
      $r("Fizz", !($i % 3)), $r("Buzz", !($i % 5))) == 0));
}
{% endcodeblock %}

{% codeblock fizzbuzz.sh %}
#!/usr/bin/env bash
for i in {1..100}; do
  if   [ 0 = $(($i % 15)) ]; then echo "FizzBuzz";
  elif [ 0 = $(($i %  3)) ]; then echo "Fizz";
  elif [ 0 = $(($i %  5)) ]; then echo "Buzz";
  else                       echo $i;
  fi
done
{% endcodeblock %}
