#include <iostream>
class nPOINT {
    private:
        static int length;
        int* p;
    public:
        nPOINT();
        ~nPOINT();
        void Set(int index, int val);
        int Get(int index);
        static int Length();
};
