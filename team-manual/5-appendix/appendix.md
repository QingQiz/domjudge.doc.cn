# 附录

以下几个例子展示了程序应如何获得输入，并且将结果输出。

这几个样例是下述问题的解：

    第一行一个数字，即测试数据的组数；
    每组测试数据一行，包含了一个名字(一个单词，不超过99个字符)
    对每组测试数据，每行输出一个字符串 "Hello <name>!"

    以下是样例输入输出：

|      Input        |        Output         |
|      ------       |        ------         |
|    3              |                       |
|    world          |     Hello world!      |
|    Jan            |     Hello Jan!        |
|    SantaClaus     |     Hello SantaClaus! |
|                   |                       |
 
 *注意输入第一行的 3 代表有三组测试数据*

 * 下面是C语言的解：
```c
#include <stdio.h>
int main() {
    int i, ntests;
    char name[100];
    scanf("%d\n", &ntests);
    for (i = 0; i < ntests; i++) {
        scanf("%s\n", name);
        printf("Hello %s!\n", name);
    }
}
```

* 下面是C++的解：
```c++
#include <iostream>
#include <string>
using namespace std;
int main() {
    int ntests;
    string name;
    cin >> ntests;
    for (int i = 0; i < ntests; i++) {
        cin >> name;
        cout << "Hello " << name << "!" << endl;
    }
}
```

* 下面是Java的解：
```java
import java.util.*;
class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int nTests = scanner.nextInt();
        for (int i = 0; i < nTests; i++) {
            String name = scanner.next();
            System.out.println("Hello " + name + "!");
        }
    }
}
```

* 下面是Python的解：
```python
import sys

n = int(input())

for i in range(n):
    name = sys.stdin.readline().rstrip('\n')

print('Hello %s!' % (name))
```

* 下面是C#的解：
```C#
using System;
public class Hello {
    public static void Main(string[] args) {
        int nTests = int.Parse(Console.ReadLine());
        for (int i = 0; i < nTests; i++) {
            string name = Console.ReadLine();
            Console.WriteLine("Hello "+name+"!");
        }
    }
}

```

*下面是Pascal的解：
```pascal
program example(input, output);
var
    ntests, test : integer;
    name : string[100];
begin
    readln(ntests);
    for test := 1 to ntests do
    begin
        readln(name);
        writeln('Hello ', name, '!');
    end;
end.
```

* 最后是Haskell的解：
```haskell
import Prelude
main :: IO ()
main = do input <- getContents
putStr.unlines.map (\x -> "Hello " ++ x ++ "!").tail.lines $ input
```