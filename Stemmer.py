from pyparsing import StringEnd, oneOf, FollowedBy, Optional, ZeroOrMore, SkipTo

special_words = ['was', 'have', 'whose', 'whatever', 'whichever', 'hers', 'mohamed', 'ahmed', 'hamed'
    , 'she', 'there', 'here', 'these', 'series', 'create']

irregular = {'dying': 'die', 'lying': 'lie', 'idly': 'idl', 'gently': 'gentl',
             'ugly': 'ugli', 'early': 'earli', 'only': 'onli', 'any': 'ani', 'became': 'become', 'began': 'begin',
             'begun': 'begin', 'broke': 'break', 'broken': 'break'
    , 'bought': 'buy', 'caught': 'catch', 'came': 'come', 'did': 'do', 'done': 'do', 'fed': 'feed', 'got': 'get',
             'gone': 'go', 'went': 'go', 'gave': 'give', 'given': 'give'
    , 'kept': 'keep', 'known': 'know', 'knew': 'know', 'left': 'leave', 'lost': 'lose', 'met': 'meet', 'spent': 'spend',
             'paid': 'pay', 'said': 'say', 'spent': 'spend'
    , 'swing': 'swing', 'skies': 'sky', 'dying': 'die', 'lying': 'lie', 'tying': 'tie', 'news': 'news',
             'outing': 'outing', 'proceed': 'proceed', 'exceed': 'exceed',
             'succeed': 'succeed', 'heaviness': 'heavy', 'meaningless': 'mean', 'tries': 'try'
             }

prefixes = ['un', 'uni', 'an', 'im', 'anti', 'con', 'de', 'dis', 'em', 'en', 'mis', 're', 'il', 'im', 'in', 'ir']
suffixes = ['ing', 'ed', 's', 'able', 'ful', 'ly', 'ness', 'ion', 'ment', 'er', 'es', 'ship', 'less', 'wise']

prefix_str = ' '.join(prefixes)
suffix_str = ' '.join(suffixes)

wordlist = ['gone', 'meaningless', 'happy', 'tries', 'friendship', 'impossible', 'irresponsible']

endOfString = StringEnd()    # impossible*
prefix = oneOf(prefix_str)     #
suffix = oneOf(suffix_str) + FollowedBy(endOfString)


def gram():
    return (
        ZeroOrMore(prefix)("prefixes") +
        SkipTo(suffix | endOfString)("root") +
        Optional(suffix)("suffix")
    )


for wd in wordlist:
    if wd in special_words:
        print(wd)
    elif wd in irregular.keys():
        print(wd, '---->', irregular[wd])
    else:
        res = gram().parseString(wd)
        print(wd, '---->', res.root)
