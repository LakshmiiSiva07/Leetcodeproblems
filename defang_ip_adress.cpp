//Given a valid(IPv4) IP address, return a defanged version of that IP address.
//A defanged IP address replaces every period "." with "[.]".

#include <iostream>
#include<string>
//using namespace std;

class Solution {
private:
	int i = 0;
	std::string defangaddress;
public:
	std::string defangIPaddr(std::string address) {
	
	for (i = 0; i < address.length(); i++)
	{
		if (address[i] == '.')
		{
			defangaddress.append("[.]");
		}
		else
		{
			defangaddress += address[i];
		}
	}
	return defangaddress;
	}
};

int main()
{
	Solution S1;
	std::cout << S1.defangIPaddr("10.10.10.10");
}
