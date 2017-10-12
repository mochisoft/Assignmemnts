import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import PunktSentenceTokenizer


class NLPExample():

    def __init__(self,large_paragraph):
         self.large_paragraph=large_paragraph

    def pogSentences(self):
        weche_mopog=sent_tokenize(self.large_paragraph,'english')

        return weche_mopog

    def pogWords(self):
        wach_ka_wach=word_tokenize(self.large_paragraph,'english')

        return wach_ka_wach

    def process_content(self,tokenized):
        try:
            for i in tokenized[:50]:
                words = nltk.word_tokenize(i)
                tagged = nltk.pos_tag(words)
                namedEnt = nltk.ne_chunk(tagged, binary=True)
                namedEnt.draw()

        except Exception as e:
            print(str(e))


if __name__=='__main__':

    wach_mabor="Kenyans: Lets not support extrajudicial killings irrespective of who the victim is. Some of us supported the killings of innocent men and women in Nairobi, Kisumu, Siaya, Homa Bay and Migori during the anti-IEBC protests. Reason? it was politically convenient to do so. It was too distant and therefore of no consequence to our lives."
    wach_mabor+="They were not related to us. They were not from our ethnic group. They were from a troublesome tribe. Let me explain this further. Being armed with a stone or a rungu during protests is no reason to kill the person. Death is too high a price to pay for carrying around a stone or merely taunting the police. Death is irreversible. It causes too much pain. Families sometimes sink into deeper poverty after a loved one is executed."
    wach_mabor+="Policemen have too many options. They can negotiate. They can use teargas. They can use rubber bullets. If they have to use live bullets, they can aim at immobilising  by shooting at the leg, for example, rather than snuffing life out of a fellow human being."
    wach_mabor+="Even before I get to the more recent execution of Willie Kimani, Josphat Mwendwa and Joseph Muiruri, I am still stuck at the anti-IEBC protest murders. Why did they do it. Were they under express instructions to shoot and kill? Are policemen psychologically sick? Why did a large segment of the population support the murders. How come many were silent then but are speaking out now?"
    wach_mabor+="We are somewhat a civilised modern society. Thats why we have the court system. Even those who openly support terrorist acts deserve their day in court. Praising cops when they kill people out there, some of whom may be innocent but framed, is giving people who may be psychologically sick too much power over our lives."
    wach_mabor+="The executive may be benefiting from the ill-trained, grossly incompetent and shamelessly corrupt police force (they dont qualify to be a service, yet) but if it cares even a little, it should absorb all the current cops into the civil service (disperse them here and there) and start rebuilding the police service from scratch. The force, as currently structured, is irredeemable. And they are a threat to our already fragile nationhood."

    example=NLPExample(wach_mabor)

    wach_ka_wach=example.pogSentences()

    stop_words = set(stopwords.words('english'))

    wach_mobedo_filtered = [w for w in wach_ka_wach if not w in stop_words]

    print wach_mobedo_filtered

    example.process_content(wach_mobedo_filtered)
