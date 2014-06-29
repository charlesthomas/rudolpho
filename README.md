rudolpho
========

Hacky Little Thing to Remind Me to Look at My To Do List

Disclaimer
----------
I don't expect this thing to be particularly useful to anyone else. That means
it will only be useful under very specific circumstances.

What is rudolpho?
-----------------
I use [magpie](https://github.com/charlesthomas/magpie/) as my To Do list. I
decided to create this thing as a reminder to look at my todo list every day, in
case I forget. In magpie, any line in a note that starts with "[ ]" is
considered to be an incomplete todo list item. Any line that starts with "[x]"
is considered to be a done todo list item. I have a daily todo list in magpie,
which is always titled YYYY-MM-DD (eg 2014-06-29). Since magpie just stores
notes in plaintext files, my todo list is always just a plaintext file.

What does it do?
----------------
So here's what rudolpho does:
1. Checks to see if there's a todo list for today already created. If there isn't,
   nothing happens.
1. Checks to see if there is a todo list from yesterday. If there is, prepends
   today's list with a count of the number of things done from yesterday.
1. Sends a reminder to me through [Pushover.net](https://pushover.net) (using
   [Coinshot](https://github.com/charlesthomas/coinshot))

How do I set it up?
-------------------
1. Optional (if using Python virtualenvs): ``mkvritualenv rudolpho``
1. ``pip install -r requirements.txt``
1. Rename ``config_example.rudolpho`` to ``~/.rudolpho``
1. Set the ``notes_path`` field
1. Set either ``pushover_key_path`` or ``pushover_user_key`` field (See
   [pushover_key_path versus pushover_user_key](https://github.com/charlesthomas/rudolpho#pushover_key_path-versus-pushover_user_key))
1. Optional: set ``pushover_app_key``
1. Optional: set ``date_format`` (must conform to Python
   [datetime behavior](https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior))
1. Optional: set a cron job to run rudolpho as often as you see fit

pushover_key_path versus pushover_user_key
------------------------------------------
Since I use Pushover.net for other apps, I keep my user key in its own file, so
it's easy to get at it from other places. This is not required. If you don't
care, you can just put your user key in ``~/.rudolpho`` and be done with it. If
you want to put your pushover user key in a file, it should be the only thing in
the file (trailing line break is OK). In the config file, ``pushover_user_key``
takes precedence over ``pushover_key_path``.

What's with the weird name?
---------------------------
This is not the first script I've written to remind me I have stuff to do. At
some point in the past, I was trying to text someone an explanation of a
different "todo list notifier" script, and it got autocorrected to "rudolpho."
It became a running joke that any todo list notifier was referred to as
"rudolpho."
