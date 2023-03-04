// C++ Coding Standard

/// ------------------- header -----------------------

#pragma once // It's 2022, we don't need #ifdef include guards.

#include <memory> // unique_ptr and shared ptr

namespace mynamespace { // All lower-case
	
class MyClass // Camel-case with upper-case first letter
{
public:

	// Favor rule-of-0, but if you need to define any of these, do rule-of-5.
	~MyClass();
	MyClass( const MyClass &other ) = delete;
	MyClass &operator= ( const MyClass &rhs ) = delete;
	MyClass( const MyClass &&other ) = delete;
	MyClass &operator= ( const MyClass &&rhs ) = delete;


	void myInlineFunction(); // Camel-case with lower-case first letter

	void myFunction( const MyOtherClass &const, MyOtherOtherClass *outData ); // Favor pass by const-ref.

private:
	// Member variables are camel-case starting with 'm'.
	int mMyMemberVar{ 0 }; // Try to initialize variables where it makes sense.
	int *mMyRawPointer{ nullptr }; // Avoid using raw pointers like this.
	// Use unique_ptr or shared_ptr instead of raw pointers.
	std::unique_ptr<int> mMyUniquePtr; // Scoped inside this class.
	std::shared_ptr<int> mMySharedPtr; // Can be shared outside this class.

	using MyType = std::vector<int>; // Favor "using" statements over typedefs.

	constexpr static const int MyConstantThatMightHaveBeenAPoundDefine{ 1000 }; // Use constexpr instead of #define if you can
};

// Inlines defined outside of class declaration for readability.
inline void MyClass::myInlineFunction() { std::cerr << "yo\n"; }

}// end namespace mynamespace


/// ------------------- cpp body -----------------------

#include "MyClass.h"         // Header file for class is first include
#include <stdio.h>           // C funcs
#include <array>             // C++ funcs
#include <list>
#include <vector>            // Attempted alphabetical order bc I am OCD
#include "local_lib/MyLib.h" // Local libs
#include "LocalCode.h"       // Local code


namespace mynamespace {

void MyClass::myFunction( const MyOtherClass &const, MyOtherOtherClass *outData )
{
	bool doStuff = true;
	std::vector<MyOtherClass> containerItems = { MyOtherClass( 1 ), MyOtherClass( 2 ) };
	if( doStuff )
	{
		for( auto const &myItem : containerItems ) // Favor range-based for loops
		{                                          // iterators based for loops are still necessary for erasing items
		                                           // indices may be necessary sometimes too 
			std::cerr << myItem << "\n";
		}
	}

	*outData = MyOtherClass( 3 );
}

}// end mynamespace
