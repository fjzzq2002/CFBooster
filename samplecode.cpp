#define main fakemain
#include <bits/stdc++.h>
using namespace std;
int m,n,q;
vector<int> y;
vector<string> s,t;

void main()
{
#ifdef ONLINE_JUDGE //don't mix cin/scanf, cout/printf!
	cin.tie(0); cout.tie(0);
	ios::sync_with_stdio(0);
#endif
	cin>>n>>m;
	s.resize(n);
	for(int i=0;i<n;++i) {
		cin>>s[i];
	}
	t.resize(m);
	for(int i=0;i<m;++i) {
		cin>>t[i];
	}
	cin>>q;
	y.resize(q);
	for(int i=0;i<q;++i) {
		cin>>y[i];
		--y[i]; cout<<s[y[i]%n]<<t[y[i]%m]<<"\n";
	}
	
}


#undef main
#ifndef ONLINE_JUDGE
void rmv_() {remove("IN_TEMP_A_26a4qsj");remove("OUT_TEMP_A_26a4qsj");} /*edit if you want to don't want your temps removed*/ vector<string> clean__booster___(string u){u.push_back('\n');vector<string> w;string c;for(auto t:u){if(t=='\n'||t=='\r'){while(c.size()&&c.back()==' ') c.pop_back();if(c.size()) w.push_back(c);c.clear();}else c.push_back(t);}return w;}int to_num__booster__(string s){int w=atoi(s.c_str());char buf[10];sprintf(buf,"%d",w);if(buf==s) return w;return -1;}int main(int argc,char**argv){vector<string> code;{std::ifstream t(__FILE__);std::stringstream buffer;buffer << t.rdbuf();t.close(); code=clean__booster___(buffer.str());}int num_samples=0;map<pair<int,int>,string> samples;{string cs="";pair<int,int> id(-1,-1);for(auto s:code){if(s.substr(0,4)=="*o* "){if(id.second!=-1)samples[id]=cs;id=make_pair(-1,-1),cs="";string g=s.substr(4);string si="Sample Input ";string so="Sample Output ";if(g.back()==':'&&g.substr(0,si.size())==si){int w=to_num__booster__(g.substr(si.size(),g.size()-si.size()-1));if(w>=1) id=make_pair(w,0);}if(g.back()==':'&&g.substr(0,so.size())==so){int w=to_num__booster__(g.substr(so.size(),g.size()-so.size()-1));if(w>=1) id=make_pair(w,1);}}else cs=cs+s+"\n";}while(samples.count(make_pair(num_samples+1,0))&&samples.count(make_pair(num_samples+1,1)))++num_samples;}if(!num_samples){fakemain();return 0;}cerr<<num_samples<<" samples. autofeed: ";cerr.flush();string u;getline(cin,u);bool cap=1,sil=0;while(1){if(u.size()&&u.back()=='r')u.pop_back(),cap=0;else if(u.size()&&u.back()=='s')u.pop_back(),sil=1,cap=0;else break;}int w=to_num__booster__(u);string in,out;rmv_();if(w>=1&&w<=num_samples){in=samples[make_pair(w,0)];out=samples[make_pair(w,1)];ofstream o("IN_TEMP_A_26a4qsj");o<<in; o.close();freopen("IN_TEMP_A_26a4qsj","r",stdin);if(cap){cerr<<"============= testcase "<<w<<" (captured) ============="<<endl;freopen("OUT_TEMP_A_26a4qsj","w",stdout);}else{cerr<<"================== testcase "<<w<<" ==================="<<endl;}}else{cap=0; cerr<<"=============== normal run ================"<<endl;}fakemain();if(w>=1&&w<=num_samples){string out_str;if(cap){fclose(stdout);std::ifstream t("OUT_TEMP_A_26a4qsj");std::stringstream buffer;buffer << t.rdbuf();t.close();cerr<<(out_str=buffer.str());}if(sil);else{cerr<<endl<<"================================================="<<endl;cerr<<"sample output:"<<endl<<out<<endl;if(cap){if(clean__booster___(out)==clean__booster___(out_str))cerr<<"compare passed!"<<endl;else cerr<<"compare failed!"<<endl;}}}fclose(stdin);rmv_();}
#else
int main(){fakemain();}
#endif
/*
*o* Sample Input 1:
10 12
sin im gye gap eul byeong jeong mu gi gyeong
yu sul hae ja chuk in myo jin sa o mi sin
14
1
2
3
4
10
11
12
13
73
2016
2017
2018
2019
2020
*o* Sample Output 1:
sinyu
imsul
gyehae
gapja
gyeongo
sinmi
imsin
gyeyu
gyeyu
byeongsin
jeongyu
musul
gihae
gyeongja
*o* This chunk of comment is used for auto-testing. Please don't modify.
*/
