male(shantanu).
male(bhishma).
male(chitraganda).
male(vichitravirya).
male(pandu).
male(dhritarashtra).
male(karna).
male(duryodhana).
male(dhusasana).
male(yudhishthira).
male(bhima).
male(arjuna).
male(nakula).
male(sahadeva).
male(krishna).
male(surya).
male(sutasoma).
male(maurvi).
male(shrutakarna).
male(sarvaga).
male(parikshit).
male(abhimanyu).
male(ghatotkacha).
male(pradyumna).
male(pratirindhya).
male(ashwathama).
male(drona).

female(duhshala).
female(satyavati).
female(ganga).
female(amba).
female(ambika).
female(ambalika).
female(kunti).
female(gandhari).
female(draupadi).
female(madri).
female(hidimbi).
female(subhadra).
female(uttara).
female(kausalya).
female(kripi).
female(valandhara).

parent(shantanu,bhishma).
parent(ganga,bhishma).
parent(shantanu,chitraganda).
parent(satyavati,chitraganda).
parent(shantanu,vichitravirya).
parent(satyavati,vichitravirya).
parent(kashya,amba).
parent(kausalya,amba).
parent(kashya,ambika).
parent(kausalya,ambika).
parent(kashya,ambalika).
parent(kausalya,ambalika).
parent(vichitravirya, dhritarashtra).
parent(ambika,dhritarashtra).
parent(vichitravirya, pandu).
parent(ambalika,pandu).
parent(pandu, yudhishthira).
parent(pandu, bhima).
parent(pandu, arjuna).
parent(pandu, nakula).
parent(pandu, sahadeva).
parent(dhritarashtra, duryodhana).
parent(dhritarashtra, dushasana).
parent(dhritarashtra, duhshala).
parent(kunti, yudhishthira).
parent(kunti, bhima).
parent(kunti, arjuna).
parent(madri, nakula).
parent(madri, sahadeva).
parent(gandhari, duryodhana).
parent(gandhari, dushasana).
parent(gandhari, duhshala).
parent(kunti, karna).
parent(surya, karna).
parent(bhima, ghatotkacha).
parent(hidimbi, ghatotkacha).
parent(arjuna, abhimanyu).
parent(subhadra, abhimanyu).
parent(bhima,sutasoma).
parent(draupadi,sutasoma).
parent(bhima,sarvaga).
parent(valandhara,sarvaga).
parent(yudhishthira,pratirindhya).
parent(draupadi,pratirindhya).
parent(arjuna,shrutakarna).
parent(draupadi,shrutakarna).
parent(drona,ashwathama).
parent(kripi,ashwathama).
parent(ghatotkacha,maurvi).
parent(abhimanyu,parikshit).
parent(uttara,parikshit).

% Rules
father(X, Y) :- male(X), parent(X, Y).
mother(X, Y) :- female(X), parent(X, Y).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
brother(X, Y) :- male(X), sibling(X, Y).
sister(X, Y) :- female(X), sibling(X, Y).
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
grandfather(X, Z) :- male(X), grandparent(X, Z).
grandmother(X, Z) :- female(X), grandparent(X, Z).
ancestor(X, Z) :- parent(X, Z).
ancestor(X, Z) :- parent(X, Y), ancestor(Y, Z).
spouse(X, Y) :- parent(X, Z), parent(Y, Z), X \= Y.
husband(X,Z) :- male(X), spouse(X,Z).
wife(X,Z) :- female(X), spouse(X,Z).
