#include<iostream>

class Student{
    private:
        std::string name;
        int age;
        double gpa;

    public:
        Student(std::string name, int age, double gpa){
            this->name = name;
            this->age = age;
            this->gpa = gpa;
        }

        std::string getName(){
            return this->name;
        }

        int getAge(){
            return this->age;
        }

        double getGpa(){
            return this->gpa;
        }
};

int main(){
    Student student1("Spongebob", 25, 3.2);
    std::cout << student1.getName() << std::endl;
    std::cout << student1.getAge() << std::endl;
    std::cout << student1.getGpa() << std::endl;

    Student student2("Patrick", 40, 1.5);
    std::cout << student2.getName() << std::endl;
    std::cout << student2.getAge() << std::endl;
    std::cout << student2.getGpa() << std::endl;

    return 0;
}