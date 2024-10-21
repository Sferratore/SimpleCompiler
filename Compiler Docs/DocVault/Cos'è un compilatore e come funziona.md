Un **compilatore** è un programma che traduce il codice sorgente scritto in un linguaggio di programmazione di alto livello (come C, C++, Java, Python, ecc.) in un linguaggio macchina o in un formato eseguibile che può essere eseguito direttamente da un computer. Questa traduzione è necessaria perché i computer comprendono solo il **linguaggio macchina**, che è composto da istruzioni binarie (0 e 1) specifiche per l'architettura hardware del processore.

Il compilatore svolge questa traduzione in vari **stadi**, ciascuno con un compito specifico. Il processo di compilazione mira anche a individuare errori di sintassi e di semantica nel programma, ottimizzare il codice per migliorare le prestazioni e generare un file eseguibile efficiente.

### Come funziona un compilatore: Fasi principali

1. **Analisi lessicale (Lexical Analysis)**
    
    - L'input in questa fase è il codice sorgente. L'obiettivo è scomporlo in unità fondamentali chiamate **token**, che possono essere parole chiave (es. `if`, `for`), identificatori (nomi di variabili, funzioni), operatori (`+`, `-`, `*`, ecc.), numeri e simboli.
    - Un **analizzatore lessicale** o **lexer** legge il flusso di caratteri del codice sorgente e produce una sequenza di token.
    - Esempio: Per la stringa `x = 5 + 3;`, i token potrebbero essere `ID(x), ASSIGN(=), NUMBER(5), PLUS(+), NUMBER(3), SEMICOLON(;)`.
2. **Analisi sintattica (Syntax Analysis)**
    
    - Dopo la fase lessicale, l'**analizzatore sintattico** o **parser** prende la sequenza di token e costruisce una **struttura sintattica** o **albero di sintassi astratta (AST)**. L'AST rappresenta la struttura gerarchica del programma secondo le regole grammaticali del linguaggio.
    - Il parser verifica che la sequenza dei token rispetti la grammatica del linguaggio e rileva errori di sintassi.
    - Esempio: La stringa `x = 5 + 3;` viene trasformata in un albero che rappresenta l'assegnazione di una variabile con un'operazione aritmetica.
3. **Analisi semantica (Semantic Analysis)**
    
    - In questa fase, il compilatore verifica la **correttezza semantica** del programma. Ad esempio, controlla che le operazioni siano svolte su tipi compatibili, che le variabili siano dichiarate prima di essere utilizzate e che le funzioni siano invocate con il numero corretto di argomenti.
    - Esempio: Se si tenta di sommare un numero intero e una stringa (`5 + "ciao"`), questa fase genererebbe un errore di tipo.
4. **Generazione di codice intermedio (Intermediate Code Generation)**
    
    - Una volta completata l'analisi sintattica e semantica, il compilatore traduce il programma in una **rappresentazione intermedia (IR)**, che non è ancora linguaggio macchina ma è più vicina a quest'ultimo rispetto al codice sorgente originale.
    - L'IR è generalmente indipendente dall'architettura specifica e può essere ottimizzata ulteriormente.
    - Esempio: Un linguaggio IR potrebbe rappresentare l'operazione `x = 5 + 3;` in una forma più semplice e lineare, come un'operazione di carico dei valori nei registri e l'esecuzione dell'addizione.
5. **Ottimizzazione del codice (Code Optimization)**
    
    - Durante questa fase, il compilatore tenta di migliorare l'efficienza del codice. Le ottimizzazioni possono includere la riduzione del numero di istruzioni eseguite, l'eliminazione del codice morto, l'uso di registri in modo più efficiente e molto altro.
    - Esistono vari livelli di ottimizzazione, e non tutte le ottimizzazioni sono garantite di produrre miglioramenti significativi.
6. **Generazione di codice (Code Generation)**
    
    - In questa fase, il codice intermedio viene convertito in **linguaggio macchina** o **assembly** specifico per l'architettura hardware su cui verrà eseguito il programma.
    - La generazione del codice include la gestione della memoria, l'allocazione dei registri e la traduzione delle operazioni intermedie in istruzioni della CPU.
7. **Linking e Loading**
    
    - Se il programma utilizza librerie esterne, questa fase collega il codice generato con le librerie e le funzioni esterne, producendo un file eseguibile completo.
    - Il linker può unire diversi moduli di codice compilato (ad esempio, da file `.o` o `.obj` in C) in un unico file eseguibile.

### Tipi di compilatori

#### 1. **Compilatori tradizionali**

- **Compilatori Ahead-of-Time (AOT)**: Questi compilatori convertono l'intero codice sorgente in un file binario eseguibile prima dell'esecuzione. Una volta che il codice è stato compilato, può essere eseguito direttamente sulla macchina.
- Esempio: **C, C++**.
- **Vantaggi**: Il codice compilato è generalmente molto veloce, poiché la traduzione avviene completamente prima dell'esecuzione.
- **Svantaggi**: Il processo di compilazione può essere lungo, specialmente per progetti grandi.

#### 2. **Interpreti**

- Gli **interpreti** sono diversi dai compilatori perché eseguono il codice sorgente direttamente, senza tradurlo in un eseguibile binario prima dell'esecuzione. L'interprete analizza ed esegue il codice sorgente riga per riga.
- Esempio: **Python, Ruby, JavaScript**.
- **Vantaggi**: L'interprete consente un ciclo di sviluppo rapido, perché il codice può essere modificato ed eseguito immediatamente senza dover passare attraverso una fase di compilazione lunga.
- **Svantaggi**: Il codice interpretato è generalmente più lento rispetto al codice compilato, perché l'analisi e l'esecuzione avvengono simultaneamente.

#### 3. **Compilatori Just-In-Time (JIT)**

- I compilatori **Just-In-Time (JIT)** combinano gli approcci del compilatore e dell'interprete. Il codice sorgente viene prima compilato in una rappresentazione intermedia (come il **bytecode**), e successivamente, durante l'esecuzione, parti di questo bytecode vengono compilate in linguaggio macchina "al volo", proprio mentre vengono eseguite.
- Esempio: **Java Virtual Machine (JVM)**, **.NET CLR**, **V8 JavaScript engine**.
- **Vantaggi**: Il JIT permette di ottimizzare il codice in base alle condizioni di esecuzione effettive, producendo miglioramenti delle prestazioni dinamiche. È un compromesso tra la velocità di sviluppo dell'interprete e l'efficienza del codice compilato.
- **Svantaggi**: Il JIT può introdurre un sovraccarico di tempo al primo avvio, poiché il codice viene compilato durante l'esecuzione.
    
