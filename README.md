# Contributor Location helps you find where a repositories contributors are from :) 

Simple python script to help you find where in the world a repositories contributors are from!

You will need a github API token to use this, which you can get/learn about here: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token

Once you have the token, you need to set it as an environmental variable:

```
export GITHUB_TOKEN=thelongtokenyoujustgeneratedatgitgub
```

Takes the repo you want to review as an argument: 

```
python3 main.py docker/compose
```

It is dependent on the location that a github user stores in their profile, so the reliability of this is not super high...

Have fun :)
