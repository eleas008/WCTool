import os
import sys
def count_content(content,options=None):
    results={}

    if isinstance(content,str):
        content=content.encode('utf-8')
    results['bytes']=len(content)
    results['lines']=content.count(b'\n')
    text=content.decode('utf-8',errors='replace')  
    results['words']=len([word for word in text.split() if word]) 
    results['chars']=len(text) 

    if options is None or len(options)==0:
        return f"{results['lines']} {results['words']} {results['bytes']}"
    else:
        output=[]
        if 'l' in options:
            output.append(str(results['lines']))
        if 'w' in options:
            output.append(str(results['words']))
        if 'm' in options:
            output.append(str(results['chars']))
        if 'c' in options:
            output.append(str(results['bytes']))
        return ' '.join(output)

def process_file(f_name,options=None):
    try:
        with open(f_name,'rb') as f:
            content=f.read()
            results=count_content(content,options)
            return f"{results} {f_name}"
    except IOError as e:
        print(f"Error: {e}",f=sys.stderr)
        sys.exit(1)
    
def ccwc():
    args=sys.argv[1:]
    options=set()
    f_name=None
    for arg in args:
        if arg.startswith('-') and len(arg)>1:
            for c in arg[1:]:
                options.add(c)
        else:
            f_name=arg
            break
    if not sys.stdin.isatty():
        content=sys.stdin.buffer.read()
        cc=count_content(content,options)
        print(cc)
    elif f_name:
        if not os.path.isfile(f_name):
            print(f"{f_name}: No such file")
            sys.exit(1)
        print(process_file(f_name,options))
    else:
        print("Usage: ccwc.py [-c|-l|-w|-m] [file]",f=sys.stderr)
        sys.exit(1)
    
if __name__ == "__main__":
    ccwc()