Own WC tool

It is a cli based tool that take input text as file or file stream and provide details about a file like number of bytes,lines,words and characters.

Use this commands to get information of test.txt which i have provided in my represitory.

1.Number of Bytes:
  ccwc -c test.txt
  342190 test.txt

2.Number of lines:
  ccwc -l test.txt
  7145 test.txt

3.Number of words:
  ccwc -w test.txt
  58164 test.txt

4.Number of characters:
  ccwc -m test.txt
  339292 test.txt
5.No option:
  ccwc test.txt
  7145   58164  342190 test.txt
6.Read from standard input
  cat test.txt | ccwc -l
  7145
