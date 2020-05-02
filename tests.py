from autoDiff import Test, Test_pool

TESTS = {
	"presubmit": Test_pool(strict=True, tests=[
		Test("", "4\n5\n$,\",.,!,+\n\",+,3,20\n\",+,1,14\n.,+,4,29\n+,!,4,30\n+,!,2,28\n\",$,2,20\n$,!,4,24\n"),
		Test("", "4\n4\n\",-,#,+\n#,+,3,15\n\",#,4,30\n+,\",3,22\n#,\",3,22\n#,\",2,17\n"),
		Test("", "4\n5\n',&,+,%,*\n*,%,3,12\n',',3,16\n+,&,1,11\n*,*,2,20\n&,%,3,25\n+,',4,25\n*,+,2,15\n"),
		Test("", "7\n2\n\",*\n\",*,2,17\n*,\",2,21\n*,*,3,12\n\",*,1,17\n*,*,2,30\n*,*,3,14\n*,\",2,17\n"),
		Test("", "4\n5\n$,\",.,!,+\n\",+,3,20\n\",+,1,14\n.,+,4,29\n+,!,4,30\n+,!,2,28\n\",$,2,20\n$,!,4,24\n"),
		Test("", "7\n3\n(,+,)\n(,),2,29\n+,+,1,14\n+,+,4,28\n),(,2,10\n+,),3,13\n),),3,15\n),(,2,16\n"),
		Test("", "8\n3\n(,$,.\n$,$,4,24\n(,.,2,12\n.,$,2,14\n(,.,1,19\n(,$,3,17\n$,$,1,19\n(,$,2,30\n"),
		Test("", "6\n5\n%,&,\",*,.\n%,*,4,24\n&,\",1,27\n&,*,2,14\n*,&,2,28\n%,&,1,29\n\",\",1,18\n"),
		Test("", "7\n4\n),#,!,'\n!,',3,17\n),',2,16\n',#,3,21\n),),3,13\n),),1,22\n!,),3,25\n),#,2,27\n"),
		Test("", "4\n5\n',-,),%,&\n-,),2,18\n),&,2,21\n%,',1,16\n',),4,22\n',-,1,25\n),-,2,12\n&,&,4,22\n")
	]),
	"basic": Test_pool(strict=True, tests=[
		Test("", "10\n2\n\",*\n\",*,2,17\n*,\",2,21\n*,*,3,12\n\",*,1,17\n*,*,2,30\n*,*,3,14\n*,\",2,17\n"),
		Test("", "2\n5\n$,\",.,!,+\n\",+,3,20\n\",+,1,14\n.,+,4,29\n+,!,4,30\n+,!,2,28\n\",$,2,20\n$,!,4,24\n"),
		Test("", "12\n3\n(,+,)\n(,),2,29\n+,+,1,14\n+,+,4,28\n),(,2,10\n+,),3,13\n),),3,15\n),(,2,16\n"),
		Test("", "3\n3\n(,$,.\n$,$,4,24\n(,.,2,12\n.,$,2,14\n(,.,1,19\n(,$,3,17\n$,$,1,19\n(,$,2,30\n"),
		Test("", "4\n5\n%,&,\",*,.\n%,*,4,24\n&,\",1,27\n&,*,2,14\n*,&,2,28\n%,&,1,29\n\",\",1,18\n"),
		Test("", "100\n4\n),#,!,'\n!,',3,17\n),',2,16\n',#,3,21\n),),3,13\n),),1,22\n!,),3,25\n),#,2,27\n"),
		Test("", "0\n4\n\",-,#,+\n#,+,3,15\n\",#,4,30\n+,\",3,22\n#,\",3,22\n#,\",2,17\n")
	]),
	"invalid": Test_pool(strict=True, tests=[
		Test("", "", brief="empty file"),
		Test("n", "4\n5\n$,\",.,!,+\n\",+,3,20\n\",+,1,14\n.,+,4,29\n+,!,4,30\n+,!,2,28\n\",$,2,20\n$,!,4,24\n", brief="1 arg"),
		Test("r", "4\n5\n$,\",.,!,+\n\",+,3,20\n\",+,1,14\n.,+,4,29\n+,!,4,30\n+,!,2,28\n\",$,2,20\n$,!,4,24\n", brief="1 non-existent file"),
		Test(" i", "4\n5\n$,\",.,!,+\n\",+,3,20\n\",+,1,14\n.,+,4,29\n+,!,4,30\n+,!,2,28\n\",$,2,20\n$,!,4,24\n", brief="3 args"),
		Test(" n n", "4\n5\n$,\",.,!,+\n\",+,3,20\n\",+,1,14\n.,+,4,29\n+,!,4,30\n+,!,2,28\n\",$,2,20\n$,!,4,24\n", brief="4 args"),
		Test("", "7.5\n5\n',-,),%,&\n-,),2,18\n),&,2,21\n%,',1,16\n',),4,22\n',-,1,25\n),-,2,12\n&,&,4,22\n", brief="decimal length"),
		Test("", "-1\n5\n',&,+,%,*\n*,%,3,12\n',',3,16\n+,&,1,11\n*,*,2,20\n&,%,3,25\n+,',4,25\n*,+,2,15\n", brief="negative length")
	])
}
