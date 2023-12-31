# Library_app

### Install

Αυτό το έργο απαιτεί τη **Python** και τις ακόλουθες βιβλιοθήκες Python να είναι εγκατεστημένες:

- [Flask] : Το κύριο πλαίσιο εργασίας Flask για τον ιστό.

- [jsonify] : Ένα εργαλείο για τη μετατροπή αντικειμένων Python σε απαντήσεις JSON.

- [request] : Παρέχει πρόσβαση σε δεδομένα αιτήματος και παραμέτρους.

- [Response] : Μας επιτρέπει να δημιουργήσουμε προσαρμοσμένες απαντήσεις HTTP.

- [session] : Χρησιμοποιείται για τη διαχείριση των συνεδριών των χρηστών.

- [PyMongo] : Παρέχει ολοκλήρωση με τη MongoDB για το Flask.

- [dumps (από bson.json_util)] : Χρησιμοποιείται για τη σειριοποίηση εγγράφων BSON σε JSON.

- [ObjectId (από bson.objectid)] : Αντιπροσωπεύει ένα ObjectId της MongoDB.

### Τρόπος λειτουργίας

Δημιουργία ενός docker image που συνδέεται με ένα container της MongoDB , εισαγωγή της βάσης δεδομένων UnipiLibrary που περιέχει τα collections "users" , "books", "reservations" στο image.
Εκκίνηση του Docker Image , εισαγωγή του κώδικα στο Visual Studio με την ονομασία app.py εκκίνηση του κώδικα με την επιλογή Flask.
Για την δοκιμή ανοίγουμε το postman και δημιουργούμε το request που επιθυμούμε να δοκιμάσουμε εισάγοντας στο url  http://127.0.0.1:5000/ + το @app route του function. πχ. για το add http://127.0.0.1:5000/add. Έπειτα, πατώντας body εισάγουμε στην επιλογή raw τις πληροφορίες σε μορφή json.


# Function 1: Δημιουργία χρήστη - def add_user():

Ο κώδικας αυτός εκτελεί τη λειτουργία προσθήκης νέου χρήστη στη βάση δεδομένων, ελέγχοντας αν το email υπάρχει ήδη στην βάση δεδομένων.

<img width="1680" alt="Screenshot 2023-08-21 at 1 19 02 PM" src="https://github.com/manostziger/YpoxreotikiErgasiaSept23_E18158_TZIGKOUNAKIS_EMMANOYIL/assets/141725868/2981006c-e394-447f-af04-eb64f6a99a41">


# Function 2: Login στο σύστημα - def login():

Ο κώδικας αυτός εκτελεί τη λειτουργία σύνδεσης ενός χρήστη σε ένα σύστημα, ελέγχοντας τα δεδομένα που δόθηκαν και επικοινωνώντας με τη βάση δεδομένων για να επαληθεύσει τον κωδικό πρόσβασης.

<img width="1680" alt="Screenshot 2023-08-21 at 1 20 26 PM" src="https://github.com/manostziger/YpoxreotikiErgasiaSept23_E18158_TZIGKOUNAKIS_EMMANOYIL/assets/141725868/87f86332-8e30-43f7-b089-5f41bdc1c328">

# Function 3: Delete χρήστη - def delete_user(user_id):

Ο κώδικας επιτρέπει στο διαχειριστή να διαγράψει έναν χρήστη από τη βάση δεδομένων. Ελέγχει το email του διαχειριστή που κάνει το αίτημα για να βεβαιωθεί ότι είναι έγκυρος διαχειριστής. Αν είναι, διαγράφει τον χρήστη με τον καθορισμένο αριθμό αναγνωριστικού (_id) από τη βάση δεδομένων. Ο κώδικας επιστρέφει αντίστοιχα μηνύματα απάντησης για να ενημερώσει τον διαχειριστή αν η διαγραφή πραγματοποιήθηκε με επιτυχία ή όχι, ανάλογα με τα αποτελέσματα της ενέργειας.


<img width="1680" alt="Screenshot 2023-08-21 at 1 31 24 PM" src="https://github.com/manostziger/YpoxreotikiErgasiaSept23_E18158_TZIGKOUNAKIS_EMMANOYIL/assets/141725868/27624717-f9d1-42e3-9aa3-15cbe9e1fc21">

# Function 4 : Logout από το σύστημα - def logout():

Ο κώδικας επιτρέπει σε έναν χρήστη να αποσυνδεθεί με την παροχή του email, εκτελώντας την αποσύνδεση και επιστρέφοντας το μήνυμα "User logged out successfully".

<img width="1680" alt="Screenshot 2023-08-21 at 1 29 08 PM" src="https://github.com/manostziger/YpoxreotikiErgasiaSept23_E18158_TZIGKOUNAKIS_EMMANOYIL/assets/141725868/1afc2590-ccf8-40f2-ad37-32d1590ee140">


# Function 5 : Προσθήκη βιβλίου - def add_book():

Ο κώδικας επιτρέπει σε ένα διαχειριστή (admin) να προσθέσει ένα βιβλίο στη βάση δεδομένων. Ελέγχει αν υπάρχει ήδη ένα βιβλίο με τον ίδιο τίτλο και αν ναι, επιστρέφει ένα μήνυμα για διπλή εγγραφή. Στη συνέχεια, προσθέτει το νέο βιβλίο με τα στοιχεία που παρέχονται και επιστρέφει μήνυμα επιτυχίας. Αν ο χρήστης δεν είναι διαχειριστής, επιστρέφει μήνυμα που αναφέρει ότι μόνο οι διαχειριστές μπορούν να προσθέσουν βιβλία.

<img width="1680" alt="Screenshot 2023-08-21 at 1 30 46 PM" src="https://github.com/manostziger/YpoxreotikiErgasiaSept23_E18158_TZIGKOUNAKIS_EMMANOYIL/assets/141725868/952c0c3c-a9f7-4eff-875f-9508d40277a3">

# Function 6 : Διαγραφή βιβλίου - def delete_book(book_id):

Ο κώδικας επιτρέπει σε έναν διαχειριστή (admin) να διαγράψει ένα βιβλίο από τη βάση δεδομένων. Ελέγχει αν ο χρήστης που κάνει το αίτημα είναι διαχειριστής, και αν ναι, προχωρά με τη διαγραφή του βιβλίου. Αν η διαγραφή είναι επιτυχής, επιστρέφει μήνυμα επιτυχίας. Σε αντίθετη περίπτωση, επιστρέφει μήνυμα που αναφέρει ότι μόνο οι διαχειριστές μπορούν να διαγράψουν βιβλία.

<img width="1680" alt="Screenshot 2023-08-21 at 1 21 59 PM" src="https://github.com/manostziger/YpoxreotikiErgasiaSept23_E18158_TZIGKOUNAKIS_EMMANOYIL/assets/141725868/8deb737a-211f-45d5-bb23-dad3027cec72">

# Function 7 : Αναζήτηση βιβλίου - def search_books():

Ο κώδικας επιτρέπει σε έναν χρήστη να αναζητήσει βιβλία βάσει συγκεκριμένων κριτηρίων. Ελέγχει την ύπαρξη του χρήστη και στη συνέχεια, δημιουργεί ένα ερώτημα αναζήτησης βασισμένο στα κριτήρια που δόθηκαν. Στη συνέχεια, εκτελεί την αναζήτηση στη βάση δεδομένων και επιστρέφει τα βιβλία που ταιριάζουν με τα κριτήρια. Αν δεν βρεθούν βιβλία, επιστρέφει ένα μήνυμα ότι δεν βρέθηκαν βιβλία βάσει των κριτηρίων αναζήτησης.

<img width="1680" alt="Screenshot 2023-08-21 at 1 23 57 PM" src="https://github.com/manostziger/YpoxreotikiErgasiaSept23_E18158_TZIGKOUNAKIS_EMMANOYIL/assets/141725868/0ff4fc14-6fed-41a5-80ef-db4e41233630">

# Function 8 : Κράτηση βιβλίου - def reserve_book():

Ο κώδικας επιτρέπει σε έναν χρήστη να κρατήσει ένα βιβλίο. Ελέγχει τη διαθεσιμότητα του βιβλίου. Αν το βιβλίο είναι διαθέσιμο, υπολογίζει την ημερομηνία λήξης της κράτησης βάσει των ημερών κράτησης που ορίζονται στο βιβλίο. Στη συνέχεια, ενημερώνει τη βάση δεδομένων για τη μη διαθεσιμότητα του βιβλίου, δημιουργεί μια εγγραφή κράτησης στη συλλογή 'reservations' και επιστρέφει το ID της κράτησης μαζί με ένα μήνυμα ότι η κράτηση πραγματοποιήθηκε με επιτυχία. Αν το βιβλίο δεν είναι διαθέσιμο ή δεν βρεθεί, επιστρέφει αντίστοιχα μηνύματα λάθους.


<img width="1680" alt="Screenshot 2023-08-21 at 1 24 28 PM" src="https://github.com/manostziger/YpoxreotikiErgasiaSept23_E18158_TZIGKOUNAKIS_EMMANOYIL/assets/141725868/fda6f894-713a-4a0f-9b4a-6d88ea92fb82">


# Function 9 : Στοιχεία κράτησης - def user_reservations():

Ο κώδικας αυτός επιτρέπει σε έναν χρήστη να δει τις κρατήσεις που έχει κάνει. Αναζητά τις κρατήσεις βάσει του email που δίνεται στη διεύθυνση URL και επιστρέφει τις κρατήσεις σε μορφή λίστας. Αν δεν υπάρχουν κρατήσεις, εμφανίζει ένα μήνυμα ότι δεν βρέθηκαν κρατήσεις για τον συγκεκριμένο χρήστη.

<img width="1680" alt="Screenshot 2023-08-21 at 1 26 21 PM" src="https://github.com/manostziger/YpoxreotikiErgasiaSept23_E18158_TZIGKOUNAKIS_EMMANOYIL/assets/141725868/7aca6b60-e633-45c8-a226-615cde465dd3">

# Function 10 : Λεπτομέρειες κράτησης - def reservation_details(reservation_id):

Ο κώδικας βρίσκει τη λεπτομέρεια μιας κράτησης βάσει του μοναδικού αριθμού κράτησης (reservation_id). Αν βρεθεί η κράτηση, επιστρέφει τις πληροφορίες της κράτησης σε μορφή JSON. Αν δεν βρεθεί η κράτηση, επιστρέφει ένα μήνυμα που λέει ότι η κράτηση δεν βρέθηκε.

<img width="1680" alt="Screenshot 2023-08-21 at 1 27 11 PM" src="https://github.com/manostziger/YpoxreotikiErgasiaSept23_E18158_TZIGKOUNAKIS_EMMANOYIL/assets/141725868/87ccec9f-24ee-423b-8948-6f300c71a713">

# Function 11 : Επιστροφή βιβλίου - def return_book(reservation_id):

Ο κώδικας αναζητά μια κράτηση βάσει του αριθμού της (reservation_id). Αν βρει την κράτηση, επιστρέφει το βιβλίο πίσω στη βιβλιοθήκη και το κάνει διαθέσιμο για νέα κράτηση. Αν το βιβλίο βρεθεί και επιστραφεί επιτυχώς, εμφανίζει ένα μήνυμα επιτυχίας. Αν δεν βρει το βιβλίο ή την κράτηση, εμφανίζει μήνυμα λάθους.

<img width="1680" alt="Screenshot 2023-08-21 at 1 28 01 PM" src="https://github.com/manostziger/YpoxreotikiErgasiaSept23_E18158_TZIGKOUNAKIS_EMMANOYIL/assets/141725868/db83440a-4a5b-4127-b0cf-5e500adfaf08">


# Function 12 : Λεπτομέρειες βιβλίου για χρήστη ή διαχειριστή - def book_details(book_id):

Ο κώδικας βρίσκει πληροφορίες για ένα βιβλίο βάσει του αριθμού του (book_id) και του email του χρήστη. Εμφανίζει βασικές πληροφορίες για το βιβλίο και, αν ο χρήστης είναι διαχειριστής, προσθέτει περισσότερες πληροφορίες σχετικά με τη διαθεσιμότητα και τις κρατήσεις. Αν ο χρήστης δεν βρεθεί ή το βιβλίο δεν βρεθεί, επιστρέφονται αντίστοιχα μηνύματα λάθους.

<img width="1680" alt="Screenshot 2023-08-21 at 1 28 35 PM (1)" src="https://github.com/manostziger/YpoxreotikiErgasiaSept23_E18158_TZIGKOUNAKIS_EMMANOYIL/assets/141725868/fc0a82ad-445a-46f0-9704-3aafea53da8d">



# Flask Container:
Για το conteiner του web service, αρχικά δημιουργήθηκε ένα image για το αρχείο app.py. Για να δημιουργήσουμε το image από το Dockerfile χρησιμοποιήθηκε η εντολή:
  ```sh
       docker build -t flask_image .
  ```
## Dockerfile:
Για το image toυ web service, αρχικά εγκαταστάθηκαν τα απαραίτητα εργαλεία, python3, flask και pymongo.

## Containerization
Για το τελικό στάδιο του containerization πρέπει να συνδεθούν τα containers του web service και του MongoDB. Για αυτο δημιουργήθηκε το αρχείο docker-compose.yml.


<img width="1680" alt="Screenshot 2023-08-21 at 1 32 37 PM" src="https://github.com/manostziger/YpoxreotikiErgasiaSept23_E18158_TZIGKOUNAKIS_EMMANOYIL/assets/141725868/e88a46dc-7e94-4e87-ab7c-0331d59d3ce1">






