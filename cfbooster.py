# coding=utf8
from __future__ import print_function

# CFBooster by TLE
# Ver 0.12 (2020-01-09)
# too lazy to make gui, maybe someone can do that

# 0% deep learning
# 100% rule-based

#put your own template here!
padding="\t"
code_template= \
r"""#define main fakemain
#include <bits/stdc++.h>
using namespace std;
[VARS]
void main()
{
#ifdef ONLINE_JUDGE //don't mix cin/scanf, cout/printf!
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
#endif
[CODES]	
}


#undef main
#ifndef ONLINE_JUDGE
void rmv_() {remove("in_temp");remove("out_temp");} /*edit if you want to don't want your temps removed*/ string to_str__booster__(int x) {char buf[100];sprintf(buf,"%d",x);return buf;} vector<string> clean__booster___(string u){u.push_back('\n');vector<string> w;string c;for(auto t:u){if(t=='\n'||t=='\r'){while(c.size()&&c.back()==' ') c.pop_back();if(c.size()) w.push_back(c);c.clear();}else c.push_back(t);}return w;}int to_num__booster__(string s){int w=atoi(s.c_str());char buf[10];sprintf(buf,"%d",w);if(buf==s) return w;return -1;}int main(int argc,char**argv){if(argc==2&&(string)argv[1]=="r") {fakemain();return 0;}vector<string> code;{std::ifstream t(__FILE__);std::stringstream buffer;buffer << t.rdbuf();t.close(); code=clean__booster___(buffer.str());}int num_samples=0;map<pair<int,int>,string> samples;{string cs="";pair<int,int> id(-1,-1);for(auto s:code){if(s.substr(0,4)=="*o* "){if(id.second!=-1)samples[id]=cs;id=make_pair(-1,-1),cs="";string g=s.substr(4);string si="Sample Input ";string so="Sample Output ";if(g.back()==':'&&g.substr(0,si.size())==si){int w=to_num__booster__(g.substr(si.size(),g.size()-si.size()-1));if(w>=1) id=make_pair(w,0);}if(g.back()==':'&&g.substr(0,so.size())==so){int w=to_num__booster__(g.substr(so.size(),g.size()-so.size()-1));if(w>=1) id=make_pair(w,1);}}else cs=cs+s+"\n";}while(samples.count(make_pair(num_samples+1,0))&&samples.count(make_pair(num_samples+1,1)))++num_samples;}if(!num_samples){fakemain();return 0;}int w; int cap=1,sil=0; if(argc==2) {w=to_num__booster__(argv[1]); cerr<<w<<"... "; cap=2;} else {cerr<<num_samples<<" samples. autofeed: ";cerr.flush();string u;getline(cin,u);if(u=="a"){cerr<<"testing all samples..."<<endl;for(int i=1;i<=num_samples;++i) {cerr<<"testing sample ";int rt=system(((string)"\""+argv[0]+"\" "+to_str__booster__(i)).c_str()); if(rt) cerr<<endl<<"WA/RE (return value "<<rt<<")\n",exit(-1);}cerr<<"all samples passed!"<<endl;exit(0);}while(1){if(u.size()&&u.back()=='r')u.pop_back(),cap=0;else if(u.size()&&u.back()=='s')u.pop_back(),sil=1,cap=0;else break;}w=to_num__booster__(u);}string in,out;rmv_();if(w>=1&&w<=num_samples){in=samples[make_pair(w,0)];out=samples[make_pair(w,1)];ofstream o("in_temp");o<<in; o.close();freopen("in_temp","r",stdin);if(cap){if(cap!=2) cerr<<"============= testcase "<<w<<" (captured) ============="<<endl;freopen("out_temp","w",stdout);}else{cerr<<"================== testcase "<<w<<" ==================="<<endl;}}else{cap=0; cerr<<"=============== normal run ================"<<endl;}time_t start_time=clock(); fakemain(); time_t end_time=clock(); bool force_stop=false;if(w>=1&&w<=num_samples){string out_str;if(cap){fclose(stdout);std::ifstream t("out_temp");std::stringstream buffer;buffer << t.rdbuf();t.close();out_str=buffer.str();if(cap!=2) cerr<<out_str;}if(sil);else{if(cap!=2) cerr<<endl<<"================================================="<<endl<<"sample output:"<<endl<<out<<endl;if(cap){if(clean__booster___(out)==clean__booster___(out_str))cerr<<"compare passed ("<<int((end_time - start_time)*1000.0/CLOCKS_PER_SEC+0.5)<<"ms)!"<<endl;else {cerr<<"compare failed ("<<int((end_time - start_time)*1000.0/CLOCKS_PER_SEC+0.5)<<"ms)!"<<endl; force_stop=true; if(cap==2) {cerr<<"=============== your output ==============="<<endl<<out_str<<endl<<"============== sample output =============="<<endl<<out<<endl;}}}}}fclose(stdin);rmv_(); if(force_stop) exit(-1);}
#else
int main(){fakemain();}
#endif
"""
#If you use a proxy...

'''
http_proxy  = "http://127.0.0.1:8118"
https_proxy = "https://127.0.0.1:8118"

proxyDict = {"http": http_proxy, "https": https_proxy}
'''

proxyDict=None

from bs4 import BeautifulSoup
import requests
import random
import string
import sys
import os
round='1284'
try:
    reload(sys)
    sys.setdefaultencoding('UTF8')
except:
    pass
if len(sys.argv)>=2:
    round=str(int(sys.argv[1]))
else:
    print('input round number: ',end='')
    try:
        input = raw_input
    except NameError:
        pass
    round=input()
print('round',round)
r=requests.get('https://codeforces.com/contest/'+round+'/problems', proxies=proxyDict)
print('fetched full problemset. length '+str(len(r.text)))
soup = BeautifulSoup(r.text, 'html.parser')
l=soup.find_all(class_='problemindexholder')
pro={}
for c in l:
    pro[c['problemindex']]=c
problems=list(pro.keys())
problems.sort()
print('found problems: '+','.join(problems))
#from https://stackoverflow.com/questions/3041986/apt-command-line-interface-like-yes-no-input
def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")
def write_file(fn,code):
    if os.path.exists(fn):
        if not query_yes_no(' '+fn+' already exists. Overwrite?',default="no"):
            print('skipped writing '+fn+'.')
            return
    print('writing to '+fn+' ... ',end='')
    f = open(fn,"w")
    f.write(code)
    f.close()
    print('succeed.')
#0: integer, 1: double, 2: string
def guess_type(si):
    try:
        u=int(si)
        if u>=-(1<<31) and u<(1<<31):
            return 0
        raise Exception("too big for int")
    except:
        try:
            u=int(si)
            if u>=-(1<<63) and u<(1<<63):
                return 1
            raise Exception("too big for long")
        except:
            try:
                float(si)
                return 2
            except:
                try:
                    str(si)
                    return 3
                except:
                    raise Exception("Unknown Type")
#stupid lexer
#will guess all types by samples
#will also try to guess if there's multiple test cases
#can only handle 1d input at the moment (because i'm lazy)
def lex(pn):
    is_arr={}
    var_type={}
    program=[]
    first_var=''
    for inputs in pro[pn].find_all(class_='input-specification'):
        ts=''
        for v in inputs:
            if v.get_text(separator="\n")!='':
                ts=ts+v.get_text(separator="\n")+' . '
        ts=ts.replace('\r',' . ')
        ts=ts.replace('\n',' . ')
        ts=ts.replace('...','\\cdots')
        ts=ts.replace('..','\\cdots')
        ts=ts.lower().replace(';',',').split('.')
        for u_ in ts:
            u=" "+u_+" "
            if (u.find(' line')!=-1 or u.find(' test ')!=-1 or u.find(' testcase')!=-1) and (u.find(' contain')!=-1 or u.find(' in ')!=-1):
                pass
            else:
                continue
            #?-th
            u=u.replace('-th ',' th ')
            while u.find(' th ')!=-1:
                c=u.find(' th ')
                u=u[:c]+u[c+3:]
                while c and u[c]==' ':
                    c-=1
                if c>=2 and u[c]=='$' and u[c-1]=='$' and u[c-2]=='$':
                    c-=2
                    u=u[:c]+"##"+u[c:]
            u=u.replace('—',', i.e. ')
            u=u.replace('--',', i.e. ')
            u=u.replace(',',' , ')
            while u.find('  ')!=-1:
                u=u.replace('  ',' ')
            u=u.replace(', and ',' and ')
            u=u.split(',')
            uu=[]
            for c_ in u:
                c=' '+c_+' '
                if c.find(' i.e')!=-1:
                    c=c[:c.find(' i.e')]
                if c.find(' where')!=-1:
                    c=c[:c.find(' where')]
                if c.find(' which')!=-1:
                    c=c[:c.find(' which')]
                if c.find(' consisting of ')!=-1:
                    c=c[:c.find(' consisting of ')]
                if c.find(' consisted of ')!=-1:
                    c=c[:c.find(' consisted of ')]
                if c.find(' who')!=-1:
                    c=c[:c.find(' who')]
                if c.find(' that')!=-1:
                    c=c[:c.find(' that')]
                if c.find(' what')!=-1:
                    c=c[:c.find(' what')]
                if c.find(' if')!=-1:
                    c=c[:c.find(' if')]
                uu.append(c)
            u=','.join(uu)
            open_par=0
            ps=""
            for c in u:
                if c=='(':
                    open_par+=1
                elif c==')':
                    open_par-=1
                elif open_par==0:
                    ps+=c
            ps=ps.split('$$$')
            pg=[]
            vis=set()
            for w in range(1,len(ps),2):
                if ps[w].find('=')==-1:
                    psw=ps[w].split(',')
                    for o in psw:
                        if o.find('##')!=-1:
                            continue
                        if o.find('\\')!=-1:
                            continue
                        o=o.replace(' ','')
                        if o.find('_')!=-1:
                            o=o[:o.find('_')]
                            if o in vis:
                               continue
                            vis.add(o)
                        if o=='':
                            continue
                        if len(pg)!=0 and o.isdigit():
                            continue
                        pg.append(o)
            if len(pg)==0:
                continue
            is_loop=int(not(pg[0].isalpha() and not (pg[0] in is_arr)))
            if is_loop and len(pg)==1:
                continue
#            print(pg,is_loop)
            for w in range(is_loop,len(pg)):
                if pg[w].isalpha() and not (pg[w] in is_arr):
                    if first_var=='':
                        first_var=pg[w]
                    is_arr[pg[w]]=is_loop
                    var_type[pg[w]]=0
                else:
                    return None #error
            if is_loop:
                lo=pg[0]
                while True:
                    modi=0
                    for c in range(0,len(lo)-1):
                        if lo[c].isdigit() and lo[c+1].isalpha():
                            lo=lo[:c+1]+"*"+lo[c+1:]
                            modi=1
                            break
                    if not modi:
                        break
                program.append((lo,pg[1:]))
            else:
                program.append((None,pg[0:]))
#            print(pg,is_loop,is_arr)
    return (first_var,is_arr,var_type,program)
def parse_i(p,inputs):
    l=lex(p)
    if l==None:
        return None
    #single case?
    first_var,is_arr,var_type,program=l
#    print(program)
    var_list=list(is_arr.keys())
    var_list.sort(key=len,reverse=True)
    failed=0
    try:
        for i in inputs:
            for v in var_list:
                if is_arr[v]:
                    globals()["SIM_"+v.upper()]=[]
                else:
                    globals()["SIM_"+v.upper()]=None
            u=list(filter(None, i.replace('\n',' ').replace('\r',' ').split(' ')))[::-1]
            def readstr():
                if len(u)==0:
                    raise Exception("underflow!")
                return u.pop()
            for pg in program:
                if pg[0]==None:
                    #noloop
                    for c in pg[1]:
                        globals()["SIM_"+c.upper()]=readstr()
                        var_type[c]=max(var_type[c],guess_type(globals()["SIM_"+c.upper()]))
                else:
                    pg0=pg[0]
                    for c in var_list:
                        pg0=pg0.replace(c,'_I_N_T_(SIM_'+c.upper()+')')
                    pg0=pg0.replace('_I_N_T_','int')
                    pg0=eval(pg0)
                    if pg0<0:
                        raise Exception("negative loop!")
                    for s in range(pg0):
                        for c in pg[1]:
                            globals()["SIM_"+c.upper()].append(readstr())
                            var_type[c]=max(var_type[c],guess_type(globals()["SIM_"+c.upper()][-1]))
            if len(u)!=0:
                raise Exception("not yet red!")
    except:
        failed=1
        pass
    if failed==0:
        return (None,is_arr,var_type,program)
    if len(program)==0 or len(program[0][1])>1:
        return None
    for v in var_list:
        var_type[v]=0 #reset
    p0=program[0]
    program=program[1:]
    #multiple cases?
    failed=0
    try:
        for i in inputs:
            u=list(filter(None, i.replace('\n',' ').replace('\r',' ').split(' ')))[::-1]
            def readstr():
                if len(u)==0:
                    raise Exception("underflow!")
                return u.pop()
            pg=p0
            if pg[0]==None:
                #noloop
                for c in pg[1]:
                    globals()["SIM_"+c.upper()]=readstr()
                    var_type[c]=max(var_type[c],guess_type(globals()["SIM_"+c.upper()]))
            num_loop=int(globals()["SIM_"+first_var.upper()])
            if num_loop<0:
                raise Exception("negative loop!")
            for __loper__ in range(num_loop):
                for v in var_list:
                    if is_arr[v]:
                        globals()["SIM_"+v.upper()]=[]
                    else:
                        globals()["SIM_"+v.upper()]=None
                for pg in program:
                    if pg[0]==None:
                        #noloop
                        for c in pg[1]:
                            globals()["SIM_"+c.upper()]=readstr()
                            var_type[c]=max(var_type[c],guess_type(globals()["SIM_"+c.upper()]))
                    else:
                        pg0=pg[0]
                        for c in var_list:
                            pg0=pg0.replace(c,'_I_N_T_(SIM_'+c.upper()+')')
                        pg0=pg0.replace('_I_N_T_','int')
                        pg0=eval(pg0)
                        if pg0<0:
                            raise Exception("negative loop!")
                        for s in range(pg0):
                            for c in pg[1]:
                                globals()["SIM_"+c.upper()].append(readstr())
                                var_type[c]=max(var_type[c],guess_type(globals()["SIM_"+c.upper()][-1]))
            
            if len(u)!=0:
                raise Exception("not yet red!")
    except:
        failed=1
        pass
    if not failed:
        return (first_var,is_arr,var_type,program)
    return None
def parse(p):
    rng_str=p+'_'+''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(7))
    inputs=[]
    outputs=[]
    for tt in pro[p].find_all(class_='input'):
        strr=tt.find('pre').get_text(separator="\n")
        strr=strr.replace('\r\n','\n')
        strr=strr.replace('\r','\n')
        while strr[0]=='\n':
            strr=strr[1:]
        if strr[-1]!='\n':
            strr=strr+'\n'
        inputs.append(strr)
    for tt in pro[p].find_all(class_='output'):
        strr=tt.find('pre').get_text(separator="\n")
        strr=strr.replace('\r\n','\n')
        strr=strr.replace('\r','\n')
        while strr[0]=='\n':
            strr=strr[1:]
        if strr[-1]!='\n':
            strr=strr+'\n'
        outputs.append(strr)
    ps=parse_i(p,inputs)
    tail="/*\n"
    for w in range(len(inputs)):
        tail+="*o* Sample Input "+str(w+1)+":\n"
        tail+=inputs[w]
        tail+="*o* Sample Output "+str(w+1)+":\n"
        tail+=outputs[w]
    tail+='*o* This chunk of comment is used for auto-testing. Please don\'t modify.\n*/'
    code1=code_template.replace('[CODES]','').replace('[VARS]','')+tail
    code1=code1.replace('in_temp','IN_TEMP_'+rng_str).replace('out_temp','OUT_TEMP_'+rng_str)
    write_file(round+p+".cpp",code1)
    if ps==None:
        print('cannot parse input for problem '+p+'.')
        return
    rng_str=p+'_'+''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(7))
    first_var,is_arr,var_type,program=ps
    ints=[]
    lls=[]
    dbs=[]
    strs=[]
    int_vecs=[]
    ll_vecs=[]
    db_vecs=[]
    str_vecs=[]
    for c in is_arr.keys():
        if var_type[c]==0:
            if is_arr[c]:
                int_vecs.append(c)
            else:
                ints.append(c)
        elif var_type[c]==1:
            if is_arr[c]:
                ll_vecs.append(c)
            else:
                lls.append(c)
        elif var_type[c]==2:
            if is_arr[c]:
                db_vecs.append(c)
            else:
                dbs.append(c)
        else:
            if is_arr[c]:
                str_vecs.append(c)
            else:
                strs.append(c)
    for_var='_'
    if not 'i' in is_arr.keys():
        for_var='i'
    DEFS=""
    CODES=""
    if True: #stupid padding
        if len(ints)!=0:
            DEFS=DEFS+"int "+",".join(ints)+';\n'
        if len(lls)!=0:
            DEFS=DEFS+"long long "+",".join(lls)+';\n'
        if len(dbs)!=0:
            DEFS=DEFS+"double "+",".join(dbs)+';\n'
        if len(strs)!=0:
            DEFS=DEFS+"string "+",".join(strs)+';\n'
        if len(int_vecs)!=0:
            DEFS=DEFS+"vector<int> "+",".join(int_vecs)+';\n'
        if len(ll_vecs)!=0:
            DEFS=DEFS+"vector<long long> "+",".join(ll_vecs)+';\n'
        if len(db_vecs)!=0:
            DEFS=DEFS+"vector<double> "+",".join(db_vecs)+';\n'
        if len(str_vecs)!=0:
            DEFS=DEFS+"vector<string> "+",".join(str_vecs)+';\n'
    if first_var==None:
        for pp in program:
            if pp[0]==None:
                CODES=CODES+padding+"cin>>"+'>>'.join(pp[1])+';\n'
            else:
                for u in pp[1]:
                    CODES=CODES+padding+u+".resize("+pp[0]+");\n"
                CODES=CODES+padding+"for(int "+for_var+"=0;"+for_var+"<"+pp[0]+";++"+for_var+") {\n"+\
                padding+padding+"cin>>"+'>>'.join(list(map(lambda x:x+"["+for_var+"]",pp[1])))+";\n"+\
                padding+"}\n"
    else:
        CODES=CODES+padding+"cin>>"+first_var+';\n'
        CODES=CODES+padding+"while("+first_var+"--) {\n"
        for pp in program:
            if pp[0]==None:
                CODES=CODES+padding+padding+"cin>>"+'>>'.join(pp[1])+';\n'
            else:
                for u in pp[1]:
                    CODES=CODES+padding+padding+u+".resize("+pp[0]+");\n"
                CODES=CODES+padding+padding+"for(int "+for_var+"=0;"+for_var+"<"+pp[0]+";++"+for_var+") {\n"+\
                padding+padding+padding+"cin>>"+'>>'.join(list(map(lambda x:x+"["+for_var+"]",pp[1])))+";\n"\
                +padding+padding+"}\n"
        CODES=CODES+padding+"}\n"
    code2=code_template.replace('[CODES]',CODES).replace('[VARS]',DEFS)+tail
    code2=code2.replace('in_temp','IN_TEMP_'+rng_str).replace('out_temp','OUT_TEMP_'+rng_str)
    write_file(round+p+"-i.cpp",code2)
for o in problems:
    parse(o)
print('all done.')