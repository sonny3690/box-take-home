# box-take-home - by Sonny Mo

### Setting Up & Running

-   clone repository to directory of choice

```
git clone https://github.com/sonny3690/box-take-home.git

```

-   navigate to cloned repository

-   change permissions on run scripts (if they have not been changed already)

```
chmod a+x <file>

```

-   to run game

```
./myBoxShogi [-flag] [options]

```

-   to run tests

```
./test-runner-mac
```


### Support Scripts

```./debug```

- runs whatever file format is in `debug.in`

```./compareTests <testName>```

- runs `testcases/<testName>.in` and compares it to `testcases/<testName>.out`.

```./runTest <test>```
- runs `testcases/<test>.in`