#include <iostream>
using namespace std;
class vector
{
    private:
    int x,y,z;
    public:
    vector();
    vector(int x,int y,int z);
    vector(const vector &V);
    float magnitude();
    bool isnull();
    vector operator +(vector V);
    vector operator -(vector V);
    vector operator *(vector V);
    int operator ^(vector V);
    friend ostream& operator <<(ostream&out,const vector&V);

};