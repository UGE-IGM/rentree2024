
```python
phrases = [
    {"fr": "Paul a mangé une banane dans la cuisine.", 
     "en": "Paul ate a banana in the kitchen.", 
     "es": "Paul comió un plátano en la cocina.",
     "pt": "Paul comeu uma banana na cozinha.",
     "pl": "Paul zjadł banana w kuchni."},
    
    {"fr": "Julie a marché sur la route avec Aminata.", 
     "en": "Julie walked on the road with Aminata.", 
     "es": "Julie caminó por la carretera con Aminata.",
     "pt": "Julie andou na estrada com Aminata.",
     "pl": "Julie szła drogą z Aminatą."},
    
    {"fr": "Pierre a dormi dans la maison.", 
     "en": "Pierre slept in the house.", 
     "es": "Pierre durmió en la casa.",
     "pt": "Pierre dormiu na casa.",
     "pl": "Pierre spał w domu."},
    
    {"fr": "Les enfants sont allés sur la route.", 
     "en": "The children went on the road.", 
     "es": "Los niños fueron por la carretera.",
     "pt": "As crianças foram na estrada.",
     "pl": "Dzieci poszły drogą."},
    
    {"fr": "Un chien a dormi sur la route.", 
     "en": "A dog slept on the road.", 
     "es": "Un perro durmió en la carretera.",
     "pt": "Um cachorro dormiu na estrada.",
     "pl": "Pies spał na drodze."},
    
    {"fr": "Une banane a été dans la cuisine.", 
     "en": "A banana was in the kitchen.", 
     "es": "Un plátano estaba en la cocina.",
     "pt": "Uma banana estava na cozinha.",
     "pl": "Banana była w kuchni."},
    
    {"fr": "Des amis ont mangé dans la maison.", 
     "en": "Friends ate in the house.", 
     "es": "Unos amigos comieron en la casa.",
     "pt": "Amigos comeram na casa.",
     "pl": "Przyjaciele jedli w domu."},
    
    {"fr": "Paul et Julie ont marché dans la rue.", 
     "en": "Paul and Julie walked in the street.", 
     "es": "Paul y Julie caminaron por la calle.",
     "pt": "Paul e Julie caminharam na rua.",
     "pl": "Paul i Julie szli ulicą."},
    
    {"fr": "Pierre est allé dans la maison pour dormir.", 
     "en": "Pierre went into the house to sleep.", 
     "es": "Pierre fue a la casa a dormir.",
     "pt": "Pierre foi para a casa dormir.",
     "pl": "Pierre poszedł do domu, żeby spać."},
    
    {"fr": "Aminata a mangé une banane dans la cuisine.", 
     "en": "Aminata ate a banana in the kitchen.", 
     "es": "Aminata comió un plátano en la cocina.",
     "pt": "Aminata comeu uma banana na cozinha.",
     "pl": "Aminata zjadła banana w kuchni."},
    
    {"fr": "Les enfants ont joué dans la rue.", 
     "en": "The children played in the street.", 
     "es": "Los niños jugaron en la calle.",
     "pt": "As crianças brincaram na rua.",
     "pl": "Dzieci bawiły się na ulicy."},
    
    {"fr": "Un chat a dormi dans la maison.", 
     "en": "A cat slept in the house.", 
     "es": "Un gato durmió en la casa.",
     "pt": "Um gato dormiu na casa.",
     "pl": "Kot spał w domu."},
    
    {"fr": "Julie a marché avec Pierre sur la route.", 
     "en": "Julie walked with Pierre on the road.", 
     "es": "Julie caminó con Pierre por la carretera.",
     "pt": "Julie andou com Pierre na estrada.",
     "pl": "Julie szła z Pierre'm drogą."},
    
    {"fr": "Aminata et Julie sont allées dans la rue.", 
     "en": "Aminata and Julie went into the street.", 
     "es": "Aminata y Julie fueron a la calle.",
     "pt": "Aminata e Julie foram para a rua.",
     "pl": "Aminata i Julie poszły na ulicę."},
    
    {"fr": "Paul et Aminata ont mangé des bananes dans la cuisine.", 
     "en": "Paul and Aminata ate bananas in the kitchen.", 
     "es": "Paul y Aminata comieron plátanos en la cocina.",
     "pt": "Paul e Aminata comeram bananas na cozinha.",
     "pl": "Paul i Aminata jedli banany w kuchni."},
    
    {"fr": "Paul a mangé une poire sur la chaise.", 
     "en": "Paul ate a pear on the chair.", 
     "es": "Paul comió una pera en la silla.",
     "pt": "Paul comeu uma pêra na cadeira.",
     "pl": "Paul zjadł gruszkę na krześle."},
    
    {"fr": "Julie a dormi derrière le buffet.", 
     "en": "Julie slept behind the buffet.", 
     "es": "Julie durmió detrás del buffet.",
     "pt": "Julie dormiu atrás do buffet.",
     "pl": "Julie spała za bufetem."},
    
    {"fr": "Pierre a marché sur la route avec une poire.", 
     "en": "Pierre walked on the road with a pear.", 
     "es": "Pierre caminó por la carretera con una pera.",
     "pt": "Pierre andou na estrada com uma pêra.",
     "pl": "Pierre szedł drogą z gruszką."},
    
    {"fr": "Les enfants ont mangé des poires dans la cuisine.", 
     "en": "The children ate pears in the kitchen.", 
     "es": "Los niños comieron peras en la cocina.",
     "pt": "As crianças comeram peras na cozinha.",
     "pl": "Dzieci jadły gruszki w kuchni."},
    
    {"fr": "Un chien a dormi derrière la maison.", 
     "en": "A dog slept behind the house.", 
     "es": "Un perro durmió detrás de la casa.",
     "pt": "Um cachorro dormiu atrás da casa.",
     "pl": "Pies spał za domem."},
    
    {"fr": "Une chaise a été dans la cuisine.", 
     "en": "A chair was in the kitchen.", 
     "es": "Una silla estaba en la cocina.",
     "pt": "Uma cadeira estava na cozinha.",
     "pl": "Krzesło było w kuchni."},
    
    {"fr": "Des poires ont été sur le buffet.", 
     "en": "Pears were on the buffet.", 
     "es": "Las peras estaban en el buffet.",
     "pt": "Peras estavam no buffet.",
     "pl": "Gruszki były na bufecie."},
    
    {"fr": "Paul et Julie sont allés dans la rue derrière la maison.", 
     "en": "Paul and Julie went into the street behind the house.", 
     "es": "Paul y Julie fueron a la calle detrás de la casa.",
     "pt": "Paul e Julie foram para a rua atrás da casa.",
     "pl": "Paul i Julie poszli na ulicę za domem."},
    
    {"fr": "Pierre est allé dans la cuisine pour manger une poire.", 
     "en": "Pierre went into the kitchen to eat a pear.", 
     "es": "Pierre fue a la cocina a comer una pera.",
     "pt": "Pierre foi para a cozinha comer uma pêra.",
     "pl": "Pierre poszedł do kuchni zjeść gruszkę."},
    
    {"fr": "Aminata a marché sur la route derrière Paul.", 
     "en": "Aminata walked on the road behind Paul.", 
     "es": "Aminata caminó por la carretera detrás de Paul.",
     "pt": "Aminata andou na estrada atrás de Paul.",
     "pl": "Aminata szła drogą za Paulem."},
    
    {"fr": "Les amis ont dormi sur les chaises.", 
     "en": "The friends slept on the chairs.", 
     "es": "Los amigos durmieron en las sillas.",
     "pt": "Os amigos dormiram nas cadeiras.",
     "pl": "Przyjaciele spali na krzesłach."},
    
    {"fr": "Un chat a été derrière le buffet.", 
     "en": "A cat was behind the buffet.", 
     "es": "Un gato estaba detrás del buffet.",
     "pt": "Um gato estava atrás do buffet.",
     "pl": "Kot był za bufetem."},
    
    {"fr": "Julie a mang

é une poire sur la chaise.", 
     "en": "Julie ate a pear on the chair.", 
     "es": "Julie comió una pera en la silla.",
     "pt": "Julie comeu uma pêra na cadeira.",
     "pl": "Julie zjadła gruszkę na krześle."},
    
    {"fr": "Aminata et Julie ont marché dans la rue derrière la maison.", 
     "en": "Aminata and Julie walked in the street behind the house.", 
     "es": "Aminata y Julie caminaron por la calle detrás de la casa.",
     "pt": "Aminata e Julie caminharam na rua atrás da casa.",
     "pl": "Aminata i Julie szły ulicą za domem."},
    
    {"fr": "Paul et Aminata ont mangé des poires dans la cuisine.", 
     "en": "Paul and Aminata ate pears in the kitchen.", 
     "es": "Paul y Aminata comieron peras en la cocina.",
     "pt": "Paul e Aminata comeram peras na cozinha.",
     "pl": "Paul i Aminata jedli gruszki w kuchni."}
]
```

