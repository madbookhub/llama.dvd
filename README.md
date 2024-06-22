<img align="left" src="./github/images/llama.dvd.cover.png">

The term RAG, is always mystical to me......What words do these letters represent? And what do those words mean? To alleviate the stress from thinking, I decided to call my project as llama.DVD concisely, which means **D**ocument **V**ectorization **D**igging, constructed with the technique of RAG, and works with [llama.cpp](https://github.com/ggerganov/llama.cpp)

If you have no idea about RAG,LLM or anything related, please leave now, because following content may give you headache or lethargy.

## Principle
There are two parts:Embedding and Query. The former is used to translate your document from human language to maths language (vectorization), this is done to make it faster to look up something from the content of your document. The latter, does a little bit more work,it also translates your queries to maths language, and then finds out relevant content based on the vector dataset which was generated by previous Embedding, and passes them to LLM, finally, you get response by LLM. That is all, what RAG doing, if I am not mistaken.

May I remind you: They are independent of each other, that means, you do not have to do **Embedding** each time you query something, since the vector dataset which works for your queries is kept working once it was generated. On other hand, you should not **query** for your document before making embedding for it. In short, they don't run synchronously.

## Components
This project is made with Python, just as above description, there are two Python scripts: *vectorize.py* and *dig.py*. Perhaps you may know their functions with the names immediately.

---

**vectorize.py**, as the name suggests, generates a vector dataset based on the content of your document. Here is its arguments list:
```
-d <Name of your document,needful>
-t <Token length> (Forget it since I am not familiar with it either)
```
Copy your text document(suppose it is called "mydoc.txt") into the subfolder names *documents*, and then run this script:
```
python vectorize.py -d mydoc.txt
```
Please wait for a while, depending on the size of your document and the performance of your computer......after done, you can then check the result:
```
Mac OS/Linux>echo $?
```
or
```
Microsoft Windows>echo %ERRORLEVEL%
```
A number should be shown, if it is zero, good, otherwise, open this script with your text editor, find out the code line which contains that number, analyse it, and then do something to resolve the problem, if you are confident in your programming ability and patient, or, just remove this suite right away, don't waste your time.

---

**dig.py**, which allows you to submit queries about the content of your document to *llama.cpp server*. This is the list of arguments:
```
-q <Your query, wrapped with double quotation marks, needful>
-c <1 or higher, about the richness of content. Higher means more abundant, but slower>
```
Before you launch it, please enable *llama.cpp server* with this: 
`./server.run`

And, do this to stop *llama.cpp server*:
`./stop.run`

Don't forget to set permissions for both ".run" scripts in your Mac OS/Linux system before you execute them, like this: 
```
chmod 755 server.run
```
For Microsoft Windows system, please rename ".run" to ".bat" to instruct system how to execute them.

Once *llama.cpp server* is enabled, you can make any query about the content of your document. Following demonstrates how to query "Adam" from your "mydoc.txt":
```
python dig.py -q "Who is Adam" -c 2
```

## Supplement
Why do I create this project? Well, I try to put the technical idea of RAG into practice and see how far it can go, and, get rid of the annoying "Version Restriction", I mean, I was going to run a llama.cpp-based application that was widely acclaimed, unfortunately, it doesn't work on macOS with version earlier than 11(Big Sur), that says, it can't work on my macOS Catalina......I really don't see how the functionality of that application has much to do with the version of OS, can I get rid of the inexplicable constraints to achieve what I want?

Coding work has always followed this guiding thougt:
- less modules, less dependency.
- 

At present, this is a conceptual design, not a full-fledged application, so, it is not necessasry to compare it with others. However, it will be upgraded continuously, and your comments are welcome.
