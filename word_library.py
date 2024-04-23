#import pretty_errors 
import random

deutsch_nouns_string = """Der Mensch,Der Korper,Der Arm,Der Auge,Das Bein,Das Blut,Die Brust,Die Brust 2,Der Finger,Der Fuß,Das Gesicht,Das Haar,Der Hals,Der Hand,Die Haut,Das Herz,Das Knie,Der Kopf,Der Korper,Der Mund,Die Nase,Das Ohr,Das Rücken,Die Zahn,Die Zunge,Der Atmen,Die Backe,Der Ellbogen,Die Faust,Das Gelenk,Das Gehirn,Das Kinn,Das Knochen,Das Lippe,Das Lange,Der Magen,Der Muskel,Der Nerv,Das Shalter,Der Schweiß,Das Strin,Der Zehe,Das Aufsehen,Der Geist,Der Verstand,Das Erfahrung,Das Erinnerung,Der Gedächtnis,Der Gedanke,Der Geist,Das Kenntnis,Das Vernunft,Das Verstand,Das Charakter,Das Geduld,Das Gefuhle,Die Hoffnung,Die Stimmung,Das Freude,Das Lust,Das Angst,Der Arger,Der Schrecken,Das Sorgen,Die Trauer,Das unglücklich,Die Wut,Die Gesundheit,Die Krankheit,Die Erkältung,Der Fieber,Der Husten,Die Pille,Der Schmerz,Der Verband,Das Verletzung,Das Wunde,Der Leben,Das Tod,Die Geburt,Der Geburtstag,Das Jugend,Der Leiche,Der Gerüch,Das Schlaf,Das Träne,Das Traum,Das Korperpflege,Die Sauberkeit,Das Bad, Das Bürste,Die Creme,Die Dusche,Der Fleck,Das Handtuch,Das Kamm,Der Schmutz,Der Staub"""
english_nouns_string ="""Human being,body,arm,eye,leg,blood,chest,breast,finger,foot,face,hair,neck,hand,skin,heart,knee,head,body,mouth,nose,ear,back,teeth,tongue,breath,chick,elbow,fist,joint,brain,jaw,bone,lip,lung,stomach,muscle,nerve,shoulder,sweat,forehead,toe,apperance,mind,mind,experience,memory,memory,idea,mind,knowledge,understand,mind,character,patience,feelings,hope,mood,happiness,desire,fear,anger,panic,worry,sorrow,unhappy,rage,health,illness,cold,fever,cough,pill,pain,bandage,injury,wound,life,death,birth,birthday,youth,corpse,odor,sleep,tearm,dream,hygiene,cleaniness,bath(room),brush,creme,shower,spot,towel,comb,dirt,dust"""

deutsch_adjectives_string ="""dick,drünn,groß,hubsch,klein,schlank,schõn,bewusst,intelligent,klug,vernunftig,anständig,bescheiden,ehrlich,fleißig,geduldig,gerecht,nett,neugierig,sparsam,streng,zuverlässig,angenehm,dankbar,empfinden,erleichtert,froh,gemütlich,glücklich,angstlich,argerlish,bõse,traurig,unangenehm,verzweifelt,wutend,gesund,kräftig,krank,wohl,alt,jung,todlich,tot,müde,wach,schmutzig"""
english_adjectives_string ="""fat,thin,big,pretty,small,slender,beutiful,aware,intelligent,smart,understandable,well behaved,modest,honest,hardworking,patient,fair,nice,curious,economical,demanding,reliable,cormfortable,grateful,react,relieved,happy,pleasant,fearful,anger,anger,angry,sorrowfull,unpleasant,desperate,furious,healthy,powerful,ill,well,old,young,deadly,dead,tired,awake,dirty"""

deutsch_verbs_string ="""schwach,starz,aufpassen,denken,erfahren,erinnern,erkennen,interessieren,kennen,kõnnen,merken,missverstehen,nach dencken,vergesen,verstehen,vorstellen,empfinden,freuen,fuhlen,genießen,gern,hoffen,lächen,lächeln,lieben,bedauern,befarchten,farchten,bluten,husten,leiden,verletzen,weh tun,geboren,leben,sterben,anfassen,ansehen,bemerken,beobachten,betrachten,blicken,frieren,hõren,riechen,schauen,schwitzen,sehen,spüren,traumen,weinen,kämmen,putzen,reinigen,spülen,waschnen,wishen"""
english_verbs_string ="""weak,strong,look at,think,hear,remind,acknowledge,interesting,know,can,note,misunderstand,think about,forget,undestand,imagine,react to,happy,feel,enjoy,like to,hope,laugh,smile,love,regret,fear,fear,bleed,cough,suffer,injure,hurt,born,live,die,touch,watch,notice,observe,study,view,freeze,hear,smell,look,sweat,see,feel,dream,ery,comb,clean,dry,rinse,wash,wipe"""

deutsch_adverbs_string ="""leider"""
english_adverbs_string ="""unfortunate"""

#respective words' arrays
deutsch_nouns = deutsch_nouns_string.split(",")
english_nouns = english_nouns_string.split(",")

deutsch_adjectives = deutsch_adjectives_string.split(",")
english_adjectives = english_adjectives_string.split(",")

deutsch_verbs = deutsch_verbs_string.split(",")
english_verbs = english_verbs_string.split(",")

deutsch_adverbs = deutsch_adverbs_string.split(",")
english_adverbs = english_adverbs_string.split(",")


def translate_one(word_in):
    if word_in in deutsch_nouns:
        return english_nouns[deutsch_nouns.index(word_in)]
    elif word_in in english_nouns:
        return deutsch_nouns[english_nouns.index(word_in)]
    elif word_in in deutsch_adjectives:
        return english_adjectives[deutsch_adjectives.index(word_in)]
    elif word_in in english_adjectives:
        return deutsch_adjectives[english_adjectives.index(word_in)]
    elif word_in in deutsch_verbs:
        return english_verbs[deutsch_verbs.index(word_in)]
    elif word_in in english_verbs:
        return deutsch_verbs[english_verbs.index(word_in)]
    elif word_in in deutsch_adverbs:
        return english_adverbs[deutsch_adverbs.index(word_in)]
    elif word_in in english_adverbs:
        return deutsch_adverbs[english_adverbs.index(word_in)]
    else:
        return "Not found"


def Random_word_gen(word_type):
    if word_type == 'nouns':
        upper_limit = len(english_nouns)
        eng_array = english_nouns
        ger_array =deutsch_nouns
    elif word_type == 'verbs':
        upper_limit = len(english_verbs)
        eng_array = english_verbs
        ger_array =deutsch_verbs
    elif word_type == 'adjectives':
        upper_limit = len(english_adjectives)
        eng_array = english_adjectives
        ger_array = deutsch_adjectives
    elif word_type == 'adverbs' :
        eng_array = english_adverbs
        ger_array = deutsch_adverbs
        upper_limit = len(english_adverbs)
    else : 
        print ('invalid entry')
    return ger_array[random.randint(0,upper_limit-1)]
    
