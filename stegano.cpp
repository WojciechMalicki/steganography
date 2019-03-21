#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <fstream>
#include <cmath>

using namespace std;

int main()
{
	fstream filein, fileout;
	unsigned int x=0, i ;
	filein.open("wiele.raw", ios::binary | ios::in);
	fileout.open("wiele_out.raw", ios::binary | ios::out | ios::trunc);
	cout << filein.good() << " " << fileout.good() << endl;
	
//	if(filein.good() && fileout.good())
//	{
//		while(filein)
//		{
//			x = filein.get();
//			cout << hex << x << " ";
//			
//		}
//		
//	}
	

	cout << "size: " << i << endl;
	filein.close();
	fileout.close();
}

