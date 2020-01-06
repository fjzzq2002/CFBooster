# CFBooster

#### What's this?

A small tool that may help you a bit in Codeforces contests.

#### How to use?

Make sure you have `python`, `beautifulsoup4`, `requests` installed. It should work for both `python2` and `python3`.

Run `cfbooster.py` in your work path. Enter the round id you're taking part.

For example, if you're entering ` https://codeforces.com/contest/1279/problems`, input `1279`.

#### What can it do exactly?

|![](https://raw.githubusercontent.com/fjzzq2002/CFBooster/master/sample.gif) |
| ---- |
|see in action (speed adjusted)|

Roughly, it will read sample inputs & outputs and try to parse input format. You just need to write based on the generated code in the 'main' function and compile normally. If you want to test the i-th sample, just input i in the first line. If you only want to feed the i-th sample as input, input i followed by 'r' or 's', e.g. 2r/2s ('r' will display the sample output while 's' won't display anything more). If you just want to run normally, press enter.

#### How does it work?

The inputs & outputs are stored in the comments of the code. The program will try to read its own code by opening `__FILE__`.

Input parsing is done with some switch-cases (yes, there's no deep learning down there atm). For further details you can refer to the ~~very clumsy~~ code.

#### I want to put my own templates in!

Just open `cfbooster.py` and follow the comments.

#### I want to contribute!

If something goes wrong or something can be improved, feel free to submit an issue or open a pull request.