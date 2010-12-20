import sys,os,shutil
def h(options,buildout):
    if sys.platform.startswith('win'):
        os.chdir(options['compile-directory'])
        content = open('win32/mingwin32.mak').read()
        content = content.replace('\\exp-base.def','/exp-base.def')
        content = content.replace('\\exp-wide.def','/exp-wide.def')
        content = content.replace('type','pwd;type')
        content = content.replace('type $(BASEDEF)', 'cat ../exp-base.def')
        content = content.replace('type $(WIDEDEF)', 'cat ../exp-wide.def')
        fic = open('win32/mingwin32.mak', 'w')
        fic.write(content)
        fic.flush()
        fic.close()
def p(options,buildout):
    if sys.platform.startswith('win'):
        dest = options['location']
        orig = options['compile-directory']
        include = os.path.join(dest, 'include')
        bin = os.path.join(dest, 'bin')
        lib = os.path.join(dest, 'lib')
        for d in include, bin, lib:
            if not os.path.exists(d):
                os.makedirs(d)
        for ext in 'h', 'def':
            for d in orig, orig+'/win32':
                noecho = [shutil.copy2(os.path.join(d, f), os.path.join(include, f)) 
                          for f in os.listdir(d) 
                          if f.endswith(ext)]
        for ext in 'exe', 'def', 'dll':
            for d in orig, orig+'/win32':
                noecho = [shutil.copy2(os.path.join(d, f), os.path.join(bin, f)) 
                          for f in os.listdir(d) 
                          if f.endswith(ext)]
        for ext in 'def', 'dll':
            for d in orig, orig+'/win32':
                noecho = [shutil.copy2(os.path.join(d, f), os.path.join(lib, f)) 
                          for f in os.listdir(d) 
                          if f.endswith(ext)]
                          
        for ext in 'dll':
            for d in orig, orig+'/win32':
                noecho = [shutil.copy2(os.path.join(d, f), os.path.join(lib, f.replace('pd', '')))
                          for f in os.listdir(d) 
                          if f.endswith(ext)]
                noecho = [shutil.copy2(os.path.join(d, f), os.path.join(bin, f.replace('pd', '')))
                          for f in os.listdir(d) 
                          if f.endswith(ext)]
                          
                          
                          
                          
                          
                    
            
            
            
                
            
            

