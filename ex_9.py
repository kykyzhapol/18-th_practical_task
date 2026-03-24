from solution import StrandsDNA

covid_19 = StrandsDNA()
covid_19.add_strands('GAAT ACCGTT TTGAC TGGGAC')
print(covid_19)
covid_19.add_strands('ACCT AGGCT TGGGAC')
covid_19.add_strands('CATTTT TAATTC')
print(covid_19)
print(covid_19.get_max_strands())
