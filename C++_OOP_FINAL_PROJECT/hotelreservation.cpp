#include <iostream>
using namespace std;

//  DATE STRUCT 
struct Date {
    int day, month, year;

    bool equals(const Date* other) const {
        return day == other->day && month == other->month && year == other->year;
    }

    void print() const {
        cout << day << "/" << month << "/" << year;
    }
};

// ABSTRACT ROOM 
class Room {
protected:
    Date* reservations;
    int resCount;
    int roomId;
public:
    Room(int id) : reservations(nullptr), resCount(0), roomId(id) {}
    virtual bool isReserved(const Date* date) = 0;
    virtual void reserve(const Date* date) = 0;
    virtual void displayType() = 0;
    int getRoomId() const { return roomId; }

    virtual ~Room() {
        delete[] reservations;
    }

protected:
    bool dateExists(const Date* date) {
        for (int i = 0; i < resCount; i++) {
            if ((reservations + i)->equals(date))
                return true;
        }
        return false;
    }

    void addDate(const Date* date) {
        Date* newArr = new Date[resCount + 1];
        for (int i = 0; i < resCount; i++)
            newArr[i] = reservations[i];
        newArr[resCount] = *date;
        delete[] reservations;
        reservations = newArr;
        resCount++;
    }
};

// STANDARD SUITE 
class StandardSuite : public Room {
public:
    StandardSuite(int id) : Room(id) {}
    bool isReserved(const Date* date) {
        return dateExists(date);
    }
    void reserve(const Date* date) {
        if (!isReserved(date)) {
            addDate(date);
            cout << "Reserved Standard Suite #" << roomId << " on ";
            date->print(); cout << endl;
        } else {
            cout << "Standard Suite #" << roomId << " is already reserved on ";
            date->print(); cout << endl;
        }
    }
    void displayType() {
        cout << "Standard Suite #" << roomId << endl;
    }
};

//  PRESIDENTIAL SUITE 
class PresidentialSuite : public Room {
public:
    PresidentialSuite(int id) : Room(id) {}
    bool isReserved(const Date* date) {
        return dateExists(date);
    }
    void reserve(const Date* date) {
        if (!isReserved(date)) {
            addDate(date);
            cout << "Reserved Presidential Suite #" << roomId << " on ";
            date->print(); cout << endl;
        } else {
            cout << "Presidential Suite #" << roomId << " is already reserved on ";
            date->print(); cout << endl;
        }
    }
    void displayType() {
        cout << "Presidential Suite #" << roomId << endl;
    }
};

// ROOM MANAGER 
Room** addRoom(Room** rooms, int& size, Room* newRoom) {
    Room** newArr = new Room*[size + 1];
    for (int i = 0; i < size; i++)
        newArr[i] = rooms[i];
    newArr[size] = newRoom;
    delete[] rooms;
    size++;
    return newArr;
}

Room** removeRoom(Room** rooms, int& size, int roomId) {
    int index = -1;
    for (int i = 0; i < size; i++) {
        if (rooms[i]->getRoomId() == roomId) {
            index = i;
            break;
        }
    }
    if (index == -1) return rooms;

    Room** newArr = new Room*[size - 1];
    int j = 0;
    for (int i = 0; i < size; i++) {
        if (i != index)
            newArr[j++] = rooms[i];
        else
            delete rooms[i];  // free removed room
    }
    delete[] rooms;
    size--;
    return newArr;
}

// MAIN FUNCTION 
int main() {
    Room** rooms = nullptr;
    int roomCount = 0;

    // Create and add some rooms
    rooms = addRoom(rooms, roomCount, new StandardSuite(101));
    rooms = addRoom(rooms, roomCount, new PresidentialSuite(201));
    rooms = addRoom(rooms, roomCount, new StandardSuite(102));

    // Dates
    Date d1 = {17, 6, 2025};  // June 17, 2025
    Date d2 = {18, 6, 2025};  // June 18, 2025

    cout << "--- Reserving Rooms ---\n";
    rooms[0]->reserve(&d1); // Reserve 101
    rooms[1]->reserve(&d1); // Reserve 201
    rooms[0]->reserve(&d1); // Attempt duplicate

    cout << "\n--- Checking Availability ---\n";
    for (int i = 0; i < roomCount; i++) {
        rooms[i]->displayType();
        if (rooms[i]->isReserved(&d2)) {
            cout << "  Reserved on ";
            d2.print(); cout << "\n";
        } else {
            cout << "  Available on ";
            d2.print(); cout << "\n";
        }
    }

    cout << "\n--- Removing Room 102 ---\n";
    rooms = removeRoom(rooms, roomCount, 102);

    cout << "\n--- Remaining Rooms ---\n";
    for (int i = 0; i < roomCount; i++) {
        rooms[i]->displayType();
    }

    // Cleanup
    for (int i = 0; i < roomCount; i++)
        delete rooms[i];
    delete[] rooms;

    return 0;
}

