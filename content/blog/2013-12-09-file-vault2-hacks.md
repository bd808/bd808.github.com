Layout: post
Title: FileVault2 Hacks
Date: 2013-12-09 21:35:52 -0700
Comments: true
Github_issue_id: 21
Tags: osx, security

Mac OS X 10.7 introduced a whole disk encryption service called
[FileVault2][fv2]. This allows you to use AES 128 encryption to protect your
data. This is a great feature but it has a few small drawbacks. It uses the
password of your primary user account to unlock the system. I'm a fan of
strong passwords but for encryption I'd prefer to use a longer pass phrase for
increased entropy. Second the EFI-boot screen that is used to get the password
to decrypt the disk shows the display name of all usersthat can unlock the
system rather than blank fields for both username and password. This leaks
information that I would really rather not leak. Fortunately I've found
a little hack to work around both of these issues.

<!-- more -->

The key to my fix lies in this statement from the documentation:
> Users not enabled for FileVault unlock are only able to log into the
> computer after an unlock-enabled user has started or unlocked the drive.
> Once unlocked, the drive remains unlocked and available to all users, until
> the computer is restarted.
> <small>["OS X: About FileVault 2"][fv2]</small>

My fix is to create a new local user account that will only be used to unlock
the disk encryption key. This will provide a fix for both issues. Since this
account won't be my primary account I can give it a much longer password
without risk of [RSI][] every time that OS X prompts me for an administrator
password to install or update software. I can also give the user an innocuous
display name to be shown on the unlock screen.

1. Create a new account from the *Users & Groups* control panel:
  - New Account: Standard
  - Full Name: ************
  - Account name: encrypt
  - Password: omg this is a really long passphrase for me to remember
2. Follow the [instructions][fv2] for enabling FileVault 2 and chose the new
   user as the only user who can unlock the disk.

If you already have FileVault 2 enabled you will need to remove the decryption
right from the existing users. The easiest way I've found to do this is using
the `fdesetup` command line tool. `sudo fdesetup list` will show you the
accounts that are enabled. `sudo fdesetup remove -user bd808` will remove the
certificate for the *bd808* user.

One last step is to make the new *encrypt* user log out as soon as they log
in. This will return control to the normal OS X login system where you can
configure the login screen to display username and password prompts instead of
a list of local user accounts. There are probably several ways to do this, but
I chose to make a small application that executes this apple script command:

*logout*
``` AppleScript
ignoring application responses
  tell application "loginwindow" to «event aevtlogo»
end ignoring
```

[fv2]: http://support.apple.com/kb/ht4790
[RSI]: https://en.wikipedia.org/wiki/Repetitive_strain_injury
