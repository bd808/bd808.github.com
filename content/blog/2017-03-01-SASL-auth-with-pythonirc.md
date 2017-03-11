Title: SASL auth with python-irc
Date: 2017-03-01T06:48:04Z
Comments: True
Github_issue_id: 26
Tags: python, irc, SASL, howto

I maintain a couple of IRC bots that help out with Wikimedia devops tasks.
[Jouncebot] was a bot I started helping with when [@mattofak] moved on to
other projects. Later I developed [Stashbot] as a replacement for using the
[Logstash] [irc input plugin] that collected data for my [SAL] tool in [Tool
Labs].

Both bots are built using the awesome [irc python library] from [Jason
Coombs]. I've copied various core irc behaviors from one bot to the other as
I've discovered and fixed various bugs in how I was using the library.
I finally got around to extracting these core parts into a Python library of
it's own that I have named "IRC Bot Behavior Bundle" or [IB3] for short.

<!-- more -->

The IB3 library provides a collection of [mixin] classes that can be used to
extend an `irc.bot.SingleServerIRCBot` instance to do things like:

* Encrypt connections using SSL
* Authenticate to Freenode
* Join channels slowly to avoid flood bans
* Ping the upstream IRC server to check for connection liveness
* Rejoin channels when kicked
* Regain primary nickname after receiving a `ERR_NICKNAMEINUSE` message

All of these behaviors are pretty battle tested from months/years of use in
one or the other of my bots.

IB3 has one sexy new addition, [SASL] PLAIN authentication. SASL is an IRC v3
protocol extension that allows a client to authenticate at the time of
connection. This method lets you authenticate before your connection becomes
visible to other clients on the server. It also seems to be a bit faster than
the normal exchange with NickServ.

Making a basic bot that uses SASL auth is pretty easy using the library:

``` python
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.

import ib3.auth
import irc.bot

NICKNAME='your account name here'
PASSWORD='your password here'
CHANNELS=['##sasl_test']

class ExampleSaslBot(ib3.auth.SASL, irc.bot.SingleServerIRCBot):
    # Add your ``on_*`` handlers here
    pass

bot = ExampleSaslBot(
    server_list=[('chat.freenode.net', 6667)],
    nickname=NICKNAME,
    realname=NICKNAME,
    ident_password=PASSWORD,
    channels=CHANNELS,
)
bot.start()
```

The `ib3.auth.SASL` mixin will take care of these things for you behind the
scenes:

* Send `CAP REQ :sasl` as soon as `SingleServerIRCBot` knows it has connected
* Listen for a `CAP ACK :sasl` response from the server
* Send an `AUTHENTICATE PLAIN` message to start the auth handshake
* Wait for an `AUTHENTICATE +` response
* Send `AUTHENTICATE <base64 encoded 'username\0username\0password'>` SASL
  PLAIN request
* Wait for a `903 :SASL authentication successful` response
* Send a `CAP END` message to finish the handshake

Both Jouncebot and Stashbot have been using this code for a few weeks with no
problems yet. If you try it out and find issues, please [report a bug] and
I'll see if I can figure out how to make things work better.

[Jouncebot]: https://wikitech.wikimedia.org/wiki/Tool:Jouncebot
[@mattofak]: https://github.com/mattofak
[Stashbot]: https://wikitech.wikimedia.org/wiki/Tool:Stashbot
[Logstash]: https://www.elastic.co/products/logstash
[irc input plugin]: https://www.elastic.co/guide/en/logstash/current/plugins-inputs-irc.html
[SAL]: https://tools.wmflabs.org/sal/
[Tool Labs]: https://wikitech.wikimedia.org/wiki/Portal:Tool_Labs
[irc python library]: https://pypi.python.org/pypi/irc
[Jason Coombs]: https://github.com/jaraco
[IB3]: https://python-ib3.readthedocs.io/en/latest/index.html
[mixin]: https://en.wikipedia.org/wiki/Mixin
[SASL]: http://ircv3.net/specs/extensions/sasl-3.1.html
[report a bug]: https://github.com/bd808/python-ib3/issues
