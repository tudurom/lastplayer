# `lastplayer`

Simple program that keeps track of the last used MPRIS2 players.

## How?

It prints the order of the players, from most recent to last recent, on a single
line on `stdout` any time a player appears or disappears. The most recent list
of players is also written at `/tmp/lastplayer`.

## Why?

You can use this program to control from keybinds the most recently opened multimedia player, using for example a program like [playerctl][playerctl].

[playerctl]: https://github.com/acrisci/playerctl

Using the same technique, you may control another player based on the order of
when it was started.

## Example

Start `lastplayer` beforehand:

```bash
lastplayer &
```

Toggle the playing state of the most recent player:

```bash
#!/bin/sh

player="$(cat /tmp/lastplayer | head -n 1)"
playerctl -p $player play-pause
```
