# A sample program

A very simple program to demonstrate concepts of OOP.

## Program

```cpp
#include <iostream>
#include <memory>
#include <string>

using std::cout;

class Doctor {
  private:
    std::string name;
    int age;
    int id_no;

  public:
    Doctor(std::string name, int age, int id_no) {
        this->name = name;
        this->age = age;
        this->id_no = id_no;
    }

    std::string getName() const { return name; }
    void setName(const std::string &name) { this->name = name; }
    int getAge() const { return age; }
    void setAge(int age) { this->age = age; }
    int getIdNo() const { return id_no; }
    void setIdNo(int id_no) { this->id_no = id_no; }

    virtual void get_name() {
        cout << "Name of Doctor is " << name << std::endl;
    }

    virtual void task() { cout << "Treat patients" << std::endl; }

    Doctor(){};
    ~Doctor() { cout << "Object deleted" << std::endl; }
};

class surgeon : public Doctor {
  public:
    void task() override { cout << "Do surgery" << std::endl; }
};

class vet : public Doctor {
  private:
    int no_of_animals;

  public:
    vet(std::string name, int no_of_animals) : Doctor(name, 0, 0) {
        this->no_of_animals = no_of_animals;
    }

    void task() override { cout << "Operates on animals" << std::endl; }

    void no_animals() {
        cout << "No of Animals: " << no_of_animals << std::endl;
    }
};

int main() {
    std::unique_ptr<Doctor> rishabh =
        std::make_unique<Doctor>("Rishabh", 20, 100);
    rishabh->get_name();
    rishabh->task();

    std::unique_ptr<surgeon> amit = std::make_unique<surgeon>();
    amit->task();

    std::unique_ptr<vet> sumit = std::make_unique<vet>("Sumit", 1231);
    sumit->get_name();
    sumit->no_animals();
    sumit->task();

    return 0;
}
```
