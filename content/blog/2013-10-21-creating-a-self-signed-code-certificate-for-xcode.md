Layout: post
Title: Creating a Self-signed Code Certificate for XCode
Date: 2013-10-21 21:38
Comments: true
Github_issue_id: 18
Tags: osx, xcode, howto

I wanted to make my own build of [Textual](http://www.codeux.com/textual/)
the other day and needed a code signing certificate to complete the build.
I decided to make single, long-lived certificate to that I could reuse for
building multiple applications.

<!-- more -->

1.  Open the "Keychain Access" application

    ``` bash
    open -a "Keychain Access"
    ```

2.  Application menu > Certificate Assistant > Create a Certificate...

    ![Create a Certificate](/static/blog/create-certificate-menu.png)


3.  Configure your new certificate

    ![](/static/blog/ca-1.png)

    -  Name: Self-signed Applications
    -  Identity Type: Self Signed Root
    -  Certificate Type: Code Signing
    -  [x] Let me override defaults
    -  Continue
4.  Change expiration date

    ![](/static/blog/ca-2.png)

    - Validity Period (days): 3650
    - Continue

5.  Just keep hitting Continue to accept defaults from here on out

    ![](/static/blog/ca-last.png)

Note: Xcode seems to cache certificate info on startup. If you had XCode open while you created this certificate, restart it.

I have since used this same certificate to build
[Growl](http://growl.info/documentation/developer/growl-source-install.php)
and a couple of other apps. I'm thinking that I'll export the public
certificate and import it on my other OSX hosts so I can share the compiled
binaries from machine to machine without needing to recompile them.
