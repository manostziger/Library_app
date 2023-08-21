# YpoxreotikiErgasiaSept23_E18158_TZIGKOUNAKIS_EMMANOYIL

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

<img width="1680" alt="Screenshot 2023-08-21 at 1 19 02 PM" src="https://github.com/manostziger/YpoxreotikiErgasiaSept23_E18158_TZIGKOUNAKIS_EMMANOYIL/assets/141725868/f4e90f2b-6e02-4edd-811f-6935b6b085cd">


# Function 2: Login στο σύστημα - def login():

Ο κώδικας αυτός εκτελεί τη λειτουργία σύνδεσης ενός χρήστη σε ένα σύστημα, ελέγχοντας τα δεδομένα που δόθηκαν και επικοινωνώντας με τη βάση δεδομένων για να επαληθεύσει τον κωδικό πρόσβασης.

# Function 3: Delete χρήστη - def delete_user(user_id):

Ο κώδικας επιτρέπει στο διαχειριστή να διαγράψει έναν χρήστη από τη βάση δεδομένων. Ελέγχει το email του διαχειριστή που κάνει το αίτημα για να βεβαιωθεί ότι είναι έγκυρος διαχειριστής. Αν είναι, διαγράφει τον χρήστη με τον καθορισμένο αριθμό αναγνωριστικού (_id) από τη βάση δεδομένων. Ο κώδικας επιστρέφει αντίστοιχα μηνύματα απάντησης για να ενημερώσει τον διαχειριστή αν η διαγραφή πραγματοποιήθηκε με επιτυχία ή όχι, ανάλογα με τα αποτελέσματα της ενέργειας.

# Function 4 : Logout από το σύστημα - def logout():

Ο κώδικας επιτρέπει σε έναν χρήστη να αποσυνδεθεί με την παροχή του email, εκτελώντας την αποσύνδεση και επιστρέφοντας το μήνυμα "User logged out successfully".

# Function 5 : Προσθήκη βιβλίου - def add_book():

Ο κώδικας επιτρέπει σε ένα διαχειριστή (admin) να προσθέσει ένα βιβλίο στη βάση δεδομένων. Ελέγχει αν υπάρχει ήδη ένα βιβλίο με τον ίδιο τίτλο και αν ναι, επιστρέφει ένα μήνυμα για διπλή εγγραφή. Στη συνέχεια, προσθέτει το νέο βιβλίο με τα στοιχεία που παρέχονται και επιστρέφει μήνυμα επιτυχίας. Αν ο χρήστης δεν είναι διαχειριστής, επιστρέφει μήνυμα που αναφέρει ότι μόνο οι διαχειριστές μπορούν να προσθέσουν βιβλία.

# Function 6 : Διαγραφή βιβλίου - def delete_book(book_id):

Ο κώδικας επιτρέπει σε έναν διαχειριστή (admin) να διαγράψει ένα βιβλίο από τη βάση δεδομένων. Ελέγχει αν ο χρήστης που κάνει το αίτημα είναι διαχειριστής, και αν ναι, προχωρά με τη διαγραφή του βιβλίου. Αν η διαγραφή είναι επιτυχής, επιστρέφει μήνυμα επιτυχίας. Σε αντίθετη περίπτωση, επιστρέφει μήνυμα που αναφέρει ότι μόνο οι διαχειριστές μπορούν να διαγράψουν βιβλία.

# Function 7 : Αναζήτηση βιβλίου - def search_books():

Ο κώδικας επιτρέπει σε έναν χρήστη να αναζητήσει βιβλία βάσει συγκεκριμένων κριτηρίων. Ελέγχει την ύπαρξη του χρήστη και στη συνέχεια, δημιουργεί ένα ερώτημα αναζήτησης βασισμένο στα κριτήρια που δόθηκαν. Στη συνέχεια, εκτελεί την αναζήτηση στη βάση δεδομένων και επιστρέφει τα βιβλία που ταιριάζουν με τα κριτήρια. Αν δεν βρεθούν βιβλία, επιστρέφει ένα μήνυμα ότι δεν βρέθηκαν βιβλία βάσει των κριτηρίων αναζήτησης.

# Function 8 : Κράτηση βιβλίου - def reserve_book():

Ο κώδικας επιτρέπει σε έναν χρήστη να κρατήσει ένα βιβλίο. Ελέγχει τη διαθεσιμότητα του βιβλίου. Αν το βιβλίο είναι διαθέσιμο, υπολογίζει την ημερομηνία λήξης της κράτησης βάσει των ημερών κράτησης που ορίζονται στο βιβλίο. Στη συνέχεια, ενημερώνει τη βάση δεδομένων για τη μη διαθεσιμότητα του βιβλίου, δημιουργεί μια εγγραφή κράτησης στη συλλογή 'reservations' και επιστρέφει το ID της κράτησης μαζί με ένα μήνυμα ότι η κράτηση πραγματοποιήθηκε με επιτυχία. Αν το βιβλίο δεν είναι διαθέσιμο ή δεν βρεθεί, επιστρέφει αντίστοιχα μηνύματα λάθους.

# Function 9 : Στοιχεία κράτησης - def user_reservations():

Ο κώδικας αυτός επιτρέπει σε έναν χρήστη να δει τις κρατήσεις που έχει κάνει. Αναζητά τις κρατήσεις βάσει του email που δίνεται στη διεύθυνση URL και επιστρέφει τις κρατήσεις σε μορφή λίστας. Αν δεν υπάρχουν κρατήσεις, εμφανίζει ένα μήνυμα ότι δεν βρέθηκαν κρατήσεις για τον συγκεκριμένο χρήστη.

# Function 10 : Λεπτομέρειες κράτησης - def reservation_details(reservation_id):

Ο κώδικας βρίσκει τη λεπτομέρεια μιας κράτησης βάσει του μοναδικού αριθμού κράτησης (reservation_id). Αν βρεθεί η κράτηση, επιστρέφει τις πληροφορίες της κράτησης σε μορφή JSON. Αν δεν βρεθεί η κράτηση, επιστρέφει ένα μήνυμα που λέει ότι η κράτηση δεν βρέθηκε.

# Function 11 : Επιστροφή βιβλίου - def return_book(reservation_id):

Ο κώδικας αναζητά μια κράτηση βάσει του αριθμού της (reservation_id). Αν βρει την κράτηση, επιστρέφει το βιβλίο πίσω στη βιβλιοθήκη και το κάνει διαθέσιμο για νέα κράτηση. Αν το βιβλίο βρεθεί και επιστραφεί επιτυχώς, εμφανίζει ένα μήνυμα επιτυχίας. Αν δεν βρει το βιβλίο ή την κράτηση, εμφανίζει μήνυμα λάθους.

# Function 12 : Λεπτομέρειες βιβλίου για χρήστη ή διαχειριστή - def book_details(book_id):

Ο κώδικας βρίσκει πληροφορίες για ένα βιβλίο βάσει του αριθμού του (book_id) και του email του χρήστη. Εμφανίζει βασικές πληροφορίες για το βιβλίο και, αν ο χρήστης είναι διαχειριστής, προσθέτει περισσότερες πληροφορίες σχετικά με τη διαθεσιμότητα και τις κρατήσεις. Αν ο χρήστης δεν βρεθεί ή το βιβλίο δεν βρεθεί, επιστρέφονται αντίστοιχα μηνύματα λάθους.






