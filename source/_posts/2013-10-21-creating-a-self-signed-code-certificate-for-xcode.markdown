---
layout: post
title: "Creating a Self-signed Code Certificate for XCode"
date: 2013-10-21 21:38
comments: true
github_issue_id: 18
categories: osx xcode howto
---
I wanted to make my own build of [Textual](http://www.codeux.com/textual/)
the other day and needed a code signing certificate to complete the build.
I decided to make single, long-lived certificate to that I could reuse for
building multiple applications.

1.  Open the "Keychain Access" application

    ``` bash
    open -a "Keychain Access"
    ```

1.  Application menu > Certificate Assistant > Create a Certificate...

    ![Create a Certificate](/images/blog/create-certificate-menu.png)

<!-- more -->

1.  Configure your new certificate

    ![](/images/blog/ca-1.png)
    -  Name: Self-signed Applications
    -  Identity Type: Self Signed Root
    -  Certificate Type: Code Signing
    -  [x] Let me override defaults
    -  Continue
1.  Change expiration date

    ![](/images/blog/ca-2.png)
    - Validity Period (days): 3650
    - Continue
1.  Just keep hitting Continue to accept defaults from here on out

    ![](/images/blog/ca-last.png)

Note: Xcode seems to cache certificate info on startup. If you had XCode open while you created this certificate, restart it.

I have since used this same certificate to build
[Growl](http://growl.info/documentation/developer/growl-source-install.php)
and a couple of other apps. I'm thinking that I'll export the public
certificate and import it on my other OSX hosts so I can share the compiled
binaries from machine to machine without needing to recompile them.
