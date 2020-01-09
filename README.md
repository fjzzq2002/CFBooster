# CFBooster

#### What's this?

A small tool that may help you a bit in Codeforces contests. **(Currently C++ only)**

#### How to use?

Make sure you have `python`, `beautifulsoup4`, `requests` installed. It should work for both `python2` and `python3`.

Run `cfbooster.py` in your work path. Enter the round id you're taking part.

For example, if you're entering ` https://codeforces.com/contest/1279`, input `1279`.

Also you can call `python some/cool/path/cfbooster.py 1279` directly.

#### What can it do exactly?

|![](https://raw.githubusercontent.com/fjzzq2002/CFBooster/master/sample.gif) |
| ---- |
|see in action (speed adjusted)|

Roughly, it will read sample inputs & outputs and try to parse input format (will fail on some problems, of course). You just need to write based on the generated code in the 'main' function and compile & run normally.

After you run the binary, you can input one of the following:

+ If you want to test on all samples, input `a`.
+ If you want to test the i-th sample, just input i in the first line (your output will be compared with sample output after removing some blanks & spaces).
+ If you only want to feed the i-th sample as input, input i followed by `r` or `s`, e.g. `2r`/`2s` ('r'ead will display the sample output while 's'ilent won't display anything more).
+ If you just want to run normally, press enter.

If you want to use the binary normally, say you want to call `./program <my_in`, do it with command line argument `r`(aw): `./program r <my_in`.

Also, if you want to add more samples, you can follow the format of the comment at the end of the file.

#### How does it work?

The inputs & outputs are stored in the comments of the code. The program will try to read its own code by opening `__FILE__`. **It won't work if you moved your source file after compiling!**

Input parsing is done with some switch-cases (yes, there's no deep learning down there). For further details you can refer to the ~~very clumsy~~ code. Currently `int,long long,double,string,vector<int>,vector<long long>,vector<double>,vector<string>` are the only supported types. **The input parsing is very fragile. Check if the input is correct before you actually submit!**

#### I want to put my own templates in!

Just open `cfbooster.py` and follow the comments.

#### I want to contribute!

If something goes wrong or something can be improved, feel free to submit an issue or open a pull request.