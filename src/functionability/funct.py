# //////////////////////////////////////////////////////////////////////////////////////////
#
# BY: Jhonathan Vargas y Jose Martinez
# PROJECT: EnigmaScrypt
# V: 1.0.0
#
# Este projecto se hizo con la finalidad de ser presentado como Projecto semestral
# para la materia de Analsis y diseno de algoritmo impartida por Sharon Saldana
#
# EnigmaEncrypt es un programa enfocado a la codificacion y decodificacion de texto
# con la peculiaridad de que lo hara de una forma diferente dependiendo del dia,
# asemejando el funcionamiento de la 'Maquina Enigma', de ahi el nombre.
#
# //////////////////////////////////////////////////////////////////////////////////////////

# IMPORTANDO MODULOS
from datetime import datetime

#FECHA
date = datetime.now()
day = date.day

dic = [
    {'a':'jbz','b':'sap','c':'vht','d':'oj4','e':'flg','f':'px7','g':'s9i','h':'ter','i':'vsb','j':'5mf','k':'hzf','l':'8me','m':'kye','n':'whn','ñ':'wmg','o':'qmi','p':'494','q':'msn','r':'cqq','s':'xnd','t':'c8l','u':'qig','v':'kwu','w':'x5c','x':'cs8','y':'wfu','z':'ap4',' ':'1qf','.':'edy',',':'vf9',';':'9om','_':'zqu','-':'rfv','/':'o44','(':'zul',')':'pic','?':'umq','¿':'gug'},
    {'a':'cqf','b':'h3x','c':'ud8','d':'egx','e':'tcf','f':'mxi','g':'tyf','h':'q4e','i':'qhh','j':'ngc','k':'aza','l':'7s3','m':'wyn','n':'9ma','ñ':'xfo','o':'vvx','p':'rg6','q':'i2h','r':'pn2','s':'qy5','t':'yvv','u':'zeo','v':'eag','w':'jvz','x':'dok','y':'b6p','z':'bke',' ':'7rr','.':'hg7',',':'s8j',';':'vgl','_':'dox','-':'lgx','/':'imf','(':'1qx',')':'tlm','?':'duz','¿':'f51'},
    {'a':'iu9','b':'5j4','c':'5lm','d':'n6z','e':'vcc','f':'6zc','g':'xph','h':'ukc','i':'hcl','j':'uze','k':'fav','l':'lfg','m':'7fj','n':'byl','ñ':'9uu','o':'eo6','p':'hdx','q':'keo','r':'zcc','s':'eeu','t':'y1v','u':'46e','v':'bxf','w':'hgh','x':'2di','y':'3qq','z':'qlg',' ':'uh0','.':'4fc',',':'ug3',';':'5ky','_':'vdh','-':'kt8','/':'rr5','(':'4bi',')':'9lr','?':'geo','¿':'x7v'},
    {'a':'8ny','b':'tqj','c':'ihv','d':'bb6','e':'xv6','f':'q6h','g':'2go','h':'hmk','i':'iku','j':'sxx','k':'fdb','l':'dxs','m':'vob','n':'eyp','ñ':'nvp','o':'ynw','p':'vwa','q':'kgw','r':'zm4','s':'0lm','t':'jon','u':'hhm','v':'gpp','w':'cia','x':'gnr','y':'wik','z':'mwf',' ':'tss','.':'zsf',',':'wij',';':'c7d','_':'7cs','-':'ehx','/':'ais','(':'zfg',')':'fgc','?':'nby','¿':'o7h'},
    {'a':'byo','b':'xx6','c':'d2y','d':'hxw','e':'kpa','f':'mkg','g':'io9','h':'fmf','i':'rft','j':'snp','k':'bwg','l':'3yd','m':'4nh','n':'vog','ñ':'qtq','o':'vkh','p':'shz','q':'9bt','r':'ons','s':'uit','t':'3gw','u':'b1w','v':'zq7','w':'hu3','x':'kwd','y':'gsy','z':'olg',' ':'itg','.':'cnd',',':'wh6',';':'lq3','_':'ujv','-':'5jo','/':'r4v','(':'mca',')':'ovc','?':'fpf','¿':'k9d'},
    {'a':'xuf','b':'rl0','c':'l8c','d':'gsb','e':'l3u','f':'nki','g':'ioj','h':'arn','i':'vuz','j':'njf','k':'q1t','l':'m0p','m':'ovg','n':'wvm','ñ':'jhg','o':'1f7','p':'9ld','q':'yck','r':'wwc','s':'8k0','t':'hpp','u':'io1','v':'vln','w':'4fx','x':'xbm','y':'zww','z':'jga',' ':'lps','.':'icu',',':'yqf',';':'qjp','_':'baz','-':'d2p','/':'jle','(':'jgm',')':'zsg','?':'p1l','¿':'kwp'},
    {'a':'ksu','b':'eu4','c':'ftu','d':'has','e':'jfu','f':'ayx','g':'t0r','h':'74e','i':'s0g','j':'msu','k':'glp','l':'l8u','m':'kgv','n':'nbh','ñ':'rfp','o':'e9e','p':'meq','q':'jog','r':'9a2','s':'pkn','t':'xzl','u':'2vp','v':'fi9','w':'epf','x':'6ml','y':'w8r','z':'cjg',' ':'uip','.':'hag',',':'r2f',';':'0ki','_':'vdf','-':'iqc','/':'qdd','(':'wno',')':'vkj','?':'ldl','¿':'jml'},
    {'a':'xx2','b':'qad','c':'zcj','d':'bte','e':'c6s','f':'l9v','g':'aie','h':'b01','i':'gr3','j':'tqc','k':'9oh','l':'obb','m':'ctz','n':'tly','ñ':'piw','o':'c3a','p':'isn','q':'vph','r':'dws','s':'yax','t':'qdf','u':'kmq','v':'0sf','w':'b7n','x':'mej','y':'rgn','z':'3zh',' ':'uje','.':'xkk',',':'yny',';':'og0','_':'d6r','-':'xby','/':'en8','(':'ck6',')':'xct','?':'nf5','¿':'2ld'},
    {'a':'dws','b':'dda','c':'oni','d':'yuw','e':'xpt','f':'vah','g':'ba8','h':'3db','i':'4qm','j':'xyt','k':'018','l':'n85','m':'rzr','n':'mqr','ñ':'mx1','o':'cfj','p':'n0n','q':'afz','r':'0kg','s':'d19','t':'nvc','u':'5e1','v':'hdz','w':'2iz','x':'bkd','y':'ewe','z':'cry',' ':'ovt','.':'2tg',',':'vpg',';':'mwe','_':'osh','-':'bi1','/':'crg','(':'f3o',')':'9qr','?':'9cb','¿':'bnk'},
    {'a':'hy0','b':'1ir','c':'pfv','d':'q0t','e':'jxq','f':'kr1','g':'gqn','h':'l35','i':'qol','j':'nhg','k':'xp0','l':'kjq','m':'97d','n':'myi','ñ':'h0g','o':'v5o','p':'irr','q':'zc0','r':'99p','s':'b6h','t':'dkv','u':'44c','v':'tqt','w':'zx5','x':'9ac','y':'a0d','z':'to7',' ':'fsz','.':'rxk',',':'kqu',';':'eca','_':'wtn','-':'5yp','/':'dmm','(':'ohd',')':'oni','?':'yi4','¿':'unw'},
    {'a':'4qh','b':'gos','c':'fes','d':'h43','e':'reu','f':'z3m','g':'ths','h':'nln','i':'zlk','j':'img','k':'gj0','l':'ap9','m':'dla','n':'pi6','ñ':'znl','o':'c1d','p':'lqe','q':'u3a','r':'krx','s':'xcu','t':'w5g','u':'on5','v':'k5n','w':'mb1','x':'oiy','y':'w8c','z':'vvl',' ':'xff','.':'kvq',',':'c3g',';':'7kh','_':'ua5','-':'tnz','/':'ade','(':'ypa',')':'d63','?':'ewd','¿':'4aj'},
    {'a':'qn2','b':'w4j','c':'1sd','d':'ao3','e':'bmh','f':'8mk','g':'fcx','h':'qcw','i':'dtm','j':'l4k','k':'s5m','l':'czv','m':'idc','n':'fi3','ñ':'7d8','o':'rqv','p':'mun','q':'pzd','r':'dad','s':'pog','t':'wcg','u':'daq','v':'s28','w':'5ms','x':'wh6','y':'te7','z':'66j',' ':'e8h','.':'m25',',':'hly',';':'k9b','_':'cir','-':'5uk','/':'mpe','(':'2cb',')':'ckb','?':'hdj','¿':'lyt'},
    {'a':'llx','b':'vll','c':'ijd','d':'k6u','e':'9st','f':'haz','g':'x1e','h':'2xe','i':'wkh','j':'zxw','k':'10n','l':'lvc','m':'xvk','n':'oxz','ñ':'x9h','o':'5cj','p':'yts','q':'dkk','r':'8re','s':'nls','t':'una','u':'9i9','v':'uht','w':'7ig','x':'s5e','y':'zi7','z':'sf3',' ':'9v1','.':'jcp',',':'ndx',';':'pyr','_':'dos','-':'euy','/':'6zz','(':'i0o',')':'sdz','?':'qoz','¿':'haq'},
    {'a':'u5a','b':'5eg','c':'e8p','d':'coh','e':'gjx','f':'r9l','g':'g2c','h':'ruz','i':'511','j':'puh','k':'4gq','l':'tjt','m':'dvg','n':'yru','ñ':'zgt','o':'obq','p':'d0z','q':'mjt','r':'6ip','s':'fag','t':'zl5','u':'kfj','v':'ftc','w':'huf','x':'c50','y':'pb4','z':'m0r',' ':'ylv','.':'ctr',',':'jjn',';':'n4u','_':'sba','-':'bge','/':'rw7','(':'hhn',')':'nsj','?':'psm','¿':'oa7'},
    {'a':'ru6','b':'dnc','c':'1cn','d':'2rt','e':'d3a','f':'urs','g':'w7y','h':'h7o','i':'ux7','j':'3ho','k':'gao','l':'aro','m':'e1s','n':'mhm','ñ':'lfw','o':'hm3','p':'y5v','q':'5hq','r':'emq','s':'dr9','t':'few','u':'qlu','v':'mak','w':'t5e','x':'jlc','y':'adq','z':'xfc',' ':'5bt','.':'jua',',':'p8r',';':'qyc','_':'wnu','-':'xgy','/':'zhf','(':'ye2',')':'we1','?':'mxu','¿':'t3j'},
    {'a':'ch3','b':'nlz','c':'glp','d':'y1g','e':'w5v','f':'jkh','g':'uky','h':'wtq','i':'mex','j':'9m0','k':'ult','l':'ojp','m':'rkq','n':'ua9','ñ':'qdp','o':'ull','p':'1kt','q':'dv0','r':'uoq','s':'hpg','t':'a6q','u':'n00','v':'6ys','w':'5o5','x':'9pc','y':'rxh','z':'xtc',' ':'gob','.':'dow',',':'xfy',';':'qgg','_':'65z','-':'df4','/':'hs1','(':'guk',')':'6by','?':'kp9','¿':'16e'},
    {'a':'5oa','b':'fsi','c':'h5a','d':'xly','e':'7lq','f':'es3','g':'qmt','h':'2dj','i':'7ee','j':'btd','k':'s4v','l':'tsy','m':'jgi','n':'cfc','ñ':'3pz','o':'fww','p':'grr','q':'jkb','r':'pdx','s':'nqz','t':'tcj','u':'cyg','v':'gkk','w':'w8w','x':'ssv','y':'aiz','z':'br7',' ':'skh','.':'vxm',',':'yi6',';':'cn6','_':'11c','-':'agm','/':'0hv','(':'qx5',')':'bpx','?':'rjw','¿':'0hi'},
    {'a':'rme','b':'8ao','c':'aor','d':'zhp','e':'ihp','f':'6jk','g':'llx','h':'72z','i':'kkh','j':'bmy','k':'da0','l':'utb','m':'jmi','n':'xtj','ñ':'k01','o':'qm7','p':'pd5','q':'rfp','r':'jnh','s':'kuw','t':'lec','u':'wdg','v':'wlb','w':'qvs','x':'urb','y':'dho','z':'5yn',' ':'jao','.':'g67',',':'oni',';':'gfx','_':'xho','-':'bq4','/':'gbm','(':'eev',')':'quv','?':'ruh','¿':'fji'},
    {'a':'lvs','b':'ecb','c':'6cg','d':'bu2','e':'knd','f':'f3p','g':'bd4','h':'uae','i':'dh4','j':'i03','k':'8qq','l':'fsr','m':'hte','n':'xje','ñ':'v5h','o':'axi','p':'4mj','q':'8h5','r':'t11','s':'kn6','t':'m0q','u':'ia5','v':'frg','w':'ikc','x':'bsk','y':'xb4','z':'o1b',' ':'qer','.':'xce',',':'v0u',';':'nea','_':'wze','-':'iph','/':'rl2','(':'81q',')':'aom','?':'tsx','¿':'r1x'},
    {'a':'tob','b':'koh','c':'ko1','d':'r6p','e':'nfs','f':'fo8','g':'btg','h':'esr','i':'tpr','j':'y2y','k':'gwd','l':'jks','m':'hif','n':'von','ñ':'xce','o':'sfn','p':'ixu','q':'nce','r':'pxz','s':'xfn','t':'rrz','u':'elo','v':'slk','w':'47j','x':'31y','y':'ieh','z':'3pz',' ':'vyo','.':'0u2',',':'weg',';':'jub','_':'bdv','-':'mzw','/':'voe','(':'tbc',')':'wbl','?':'jiz','¿':'m4k'},
    {'a':'o65','b':'xer','c':'4mb','d':'d8v','e':'22v','f':'p1o','g':'bxp','h':'n8l','i':'n2u','j':'fnj','k':'3qw','l':'idn','m':'hhp','n':'knt','ñ':'kib','o':'ug4','p':'l7q','q':'1ck','r':'alp','s':'jz2','t':'ezg','u':'msy','v':'4rc','w':'ojg','x':'n8d','y':'vfs','z':'rhr',' ':'fel','.':'cbd',',':'srx',';':'kpq','_':'j0d','-':'aln','/':'fvf','(':'v0m',')':'cba','?':'zea','¿':'rcp'},
    {'a':'tyk','b':'rz2','c':'gzs','d':'duh','e':'vup','f':'zfn','g':'2ug','h':'rko','i':'6fg','j':'jxl','k':'abf','l':'mjg','m':'n9w','n':'wao','ñ':'4gr','o':'v19','p':'xyu','q':'mi3','r':'95r','s':'29d','t':'jos','u':'o4n','v':'cnd','w':'6jm','x':'m6i','y':'k8w','z':'ajy',' ':'lec','.':'2su',',':'wsv',';':'ed7','_':'msn','-':'mjy','/':'dap','(':'xg3',')':'eoe','?':'vpg','¿':'f8d'},
    {'a':'naf','b':'y9c','c':'wam','d':'xq8','e':'2eg','f':'mi8','g':'izj','h':'bny','i':'yy0','j':'lat','k':'mvo','l':'pi7','m':'bzj','n':'hbv','ñ':'jzv','o':'dyk','p':'cta','q':'tuv','r':'0n3','s':'ivh','t':'utk','u':'dry','v':'pmp','w':'6zp','x':'5wc','y':'ofg','z':'req',' ':'jvc','.':'t99',',':'8xf',';':'tle','_':'lpa','-':'t1y','/':'x4x','(':'u4m',')':'k9o','?':'dce','¿':'dir'},
    {'a':'tyd','b':'1fh','c':'uas','d':'oaf','e':'koh','f':'0he','g':'hro','h':'goj','i':'gwm','j':'rbt','k':'wao','l':'jy6','m':'p7m','n':'9bs','ñ':'zjc','o':'4an','p':'bh7','q':'7nk','r':'nnc','s':'frl','t':'gmn','u':'rls','v':'ws7','w':'kan','x':'8xh','y':'8bd','z':'oky',' ':'z9h','.':'kvu',',':'qco',';':'qxe','_':'tez','-':'pvu','/':'loy','(':'p16',')':'vvs','?':'7r5','¿':'tjt'},
    {'a':'dku','b':'pxw','c':'zug','d':'svb','e':'ujn','f':'m09','g':'nde','h':'3sd','i':'qvw','j':'crq','k':'f2u','l':'kob','m':'ucu','n':'rej','ñ':'mfa','o':'pxo','p':'vhv','q':'o9m','r':'mmg','s':'fn1','t':'9yi','u':'w4j','v':'952','w':'rv0','x':'swo','y':'job','z':'haa',' ':'6c2','.':'xee',',':'iec',';':'ako','_':'tun','-':'03h','/':'mmo','(':'yna',')':'1xu','?':'mlo','¿':'wzj'},
    {'a':'hcw','b':'twm','c':'sh9','d':'iu8','e':'t96','f':'luy','g':'34k','h':'b2f','i':'u56','j':'fxy','k':'mkb','l':'pzv','m':'3m9','n':'xua','ñ':'oaz','o':'ll7','p':'ms9','q':'5ph','r':'vvo','s':'3sx','t':'786','u':'cs3','v':'2da','w':'epd','x':'m8u','y':'ciu','z':'nqf',' ':'5t0','.':'s5k',',':'9es',';':'dcz','_':'5sj','-':'xck','/':'p63','(':'kty',')':'hds','?':'k1f','¿':'1sm'},
    {'a':'mgd','b':'ony','c':'pew','d':'bz0','e':'t22','f':'0xo','g':'myr','h':'xjn','i':'aqh','j':'dsv','k':'dxy','l':'oes','m':'apg','n':'smq','ñ':'71p','o':'ivh','p':'uhw','q':'3pb','r':'ryu','s':'pzo','t':'n7h','u':'fcp','v':'jq5','w':'riq','x':'mhw','y':'pau','z':'ewd',' ':'2t2','.':'f8z',',':'gme',';':'ab8','_':'ab0','-':'eqs','/':'vpc','(':'mxv',')':'qb6','?':'p6y','¿':'2ra'},
    {'a':'ynt','b':'fer','c':'xto','d':'g6b','e':'ksy','f':'arc','g':'nhh','h':'haa','i':'1oc','j':'ggw','k':'dld','l':'4lf','m':'brq','n':'nno','ñ':'bro','o':'ysy','p':'pmr','q':'k0x','r':'e9a','s':'nfj','t':'ql9','u':'ste','v':'d4v','w':'nfg','x':'oev','y':'co9','z':'qlp',' ':'wza','.':'tib',',':'2g9',';':'hy3','_':'x8y','-':'unm','/':'nsm','(':'mz6',')':'yoi','?':'gog','¿':'6bx'},
    {'a':'3an','b':'vnf','c':'u2c','d':'1zr','e':'3ku','f':'k0c','g':'j4n','h':'heq','i':'iz8','j':'rjr','k':'2yd','l':'0px','m':'4bz','n':'iyn','ñ':'kkf','o':'r0m','p':'hpn','q':'oy8','r':'i6o','s':'9gt','t':'mka','u':'giw','v':'kmi','w':'ork','x':'72h','y':'wkn','z':'xjq',' ':'20w','.':'izk',',':'als',';':'bov','_':'bzf','-':'fus','/':'h4q','(':'452',')':'ebl','?':'xqx','¿':'6r3'},
    {'a':'ffm','b':'der','c':'uni','d':'jc5','e':'xsm','f':'sdh','g':'s1c','h':'er8','i':'hqu','j':'cuh','k':'f5m','l':'inv','m':'hie','n':'wng','ñ':'pbn','o':'k4v','p':'f9y','q':'wcp','r':'gda','s':'ezf','t':'auq','u':'yor','v':'m70','w':'zbz','x':'eop','y':'a5t','z':'e2w',' ':'crx','.':'l5m',',':'ioh',';':'5sx','_':'3st','-':'hmm','/':'oou','(':'gsc',')':'ikw','?':'waj','¿':'yvx'},
    {'a':'bhr','b':'uug','c':'2ya','d':'iqq','e':'rz6','f':'m8o','g':'hvp','h':'hoi','i':'7pd','j':'rwx','k':'fmm','l':'mqp','m':'gzk','n':'zgb','ñ':'er2','o':'nxv','p':'nqz','q':'m7i','r':'wsh','s':'a0a','t':'v5z','u':'wom','v':'k4q','w':'h4n','x':'g8o','y':'uhm','z':'l5f',' ':'zc3','.':'l1p',',':'idw',';':'hye','_':'qhw','-':'sxn','/':'d9d','(':'xjk',')':'iey','?':'h08','¿':'zyr'}
    ]

#DICCIONARIO A USAR
d = dic[day-1]

#OBTENIENDO LA CLAVE A PARTIR DEL VALOR PRARA DECRIPTAR
def get_key(val):
    for key, value in d.items():
         if val == value:
             return key

#ENCRIPTANDO
def encriptar(x):
    x=list(x)
    for i in range(len(x)):
        for j in d:
            if x[i] == str(j):
                x[i] = d.get(j)
    return ''.join(x)

#DECRIPTANDO
def desencriptar(x):
    x=list(x)
    new_x=[]
    result = ''
    for i in range(0,len(x),3):
        element = x[i] + x[i+1] + x[i+2]
        new_x.append(element)
    for i in range(len(new_x)):
        result = result + get_key(new_x[i])
    return result