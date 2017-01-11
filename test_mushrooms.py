"""
# Testing mushrooms dataset
# https://www.csie.ntu.edu.tw/~cjlin/libsvmtools/datasets/binary.html#mushrooms
# http://archive.ics.uci.edu/ml/datasets/Mushroom

"""
from test import test_dataset


test_list = [1, 2, 3, 4, 5, 8, 10, 15, 20, 30, 50, 100, 200, 300]
bscore, b_val = test_dataset(DataSetName='mushrooms',
                             catList=range(112),
                             cl='binary',
                             TestType='number_of_trees',
                             tested_range=test_list,
                             scor='f1_macro')

bscore, b_val = test_dataset(DataSetName='mushrooms',
                             catList=range(112),
                             cl='binary',
                             TestType='number_of_attributes',
                             tested_range=range(1, 112, 3),
                             scor='f1_macro')

test_list = [1, 2, 3, 4, 5, 10, 20,  50, 100]
bscore, b_val = test_dataset(DataSetName='mushrooms',
                             catList=range(112),
                             cl='binary',
                             TestType='maximum_depth',
                             tested_range=test_list,
                             scor='accuracy')

"""
Dataset reading time: 7.474767327999871
number_of_trees test...
1  :  0.934489508874  |  0.952173243923  |  0.8966617269998096
2  :  0.921232364611  |  0.888580553663  |  1.308397826998771
3  :  0.910138557965  |  0.918842284714  |  1.980748489000689
4  :  0.901842962949  |  0.914216538016  |  2.0793266500004393
5  :  0.911769592509  |  0.896674354876  |  2.9816827380000177
8  :  0.888783667271  |  0.886723199124  |  5.063804180999796
10  :  0.916066676544  |  0.884945568719  |  5.8833891689992015
15  :  0.887228279858  |  0.895738573097  |  8.55336316300054
20  :  0.889171190886  |  0.886723199124  |  11.846346903001177
30  :  0.887598153908  |  0.891214255321  |  17.24483783299911
50  :  0.891240741988  |  0.889258712733  |  28.09600303699881
100  :  0.888219512748  |  0.886548076364  |  58.786193244999595
200  :  0.888091221735  |  0.886037605984  |  122.06210029899921
300  :  0.888091221735  |  0.888091221735  |  183.6958466570013


number_of_attributes test...
1  :  0.875952062484  |  0.887165288165  |  14.52503684200019
4  :  0.85994990949  |  0.892206616758  |  8.576715798000805
7  :  0.899680400637  |  0.88978440427  |  9.111205432000133
10  :  0.901247285039  |  0.881711361226  |  9.038469273000374
13  :  0.891826237774  |  0.904150996417  |  9.460963624000215
16  :  0.894265367432  |  0.899083465829  |  9.712238425001487
19  :  0.909744669958  |  0.908262520625  |  11.073714053000003
22  :  0.950118621731  |  0.890043963725  |  10.073536833999242
25  :  0.89290600155  |  0.907144313929  |  12.079414857000302
28  :  0.909386384175  |  0.902220175708  |  11.566888186000142
31  :  0.89702398159  |  0.906769685523  |  11.100226328000645
34  :  0.925917260106  |  0.897248427008  |  11.48484659299902
37  :  0.918014361611  |  0.903776205233  |  12.71305114200004
40  :  0.924068105981  |  0.896098252771  |  12.781816308000998
43  :  0.904038863289  |  0.914212051912  |  13.946405701999538
46  :  0.907546405627  |  0.905274307933  |  14.973352253000485
49  :  0.907590246338  |  0.897248427008  |  14.046787199999017
52  :  0.895235310894  |  0.890549230627  |  17.032291688999976
55  :  0.903412945033  |  0.895092955153  |  15.848899568998604
58  :  0.897391786127  |  0.888091221735  |  20.286067156999707
61  :  0.908409705614  |  0.891055789835  |  21.160107102001348
64  :  0.898995578871  |  0.90010513982  |  18.320969372000036
67  :  0.896378204678  |  0.900268999861  |  17.179519268998774
70  :  0.897802475102  |  0.90427588691  |  17.66553920900151
73  :  0.899597094901  |  0.883920474645  |  21.427308825999717
76  :  0.899242197943  |  0.899365496466  |  22.51635016599903
79  :  0.896413459641  |  0.895871296698  |  21.593859508000605
82  :  0.897276759627  |  0.899365496466  |  22.670828644999347
85  :  0.888381984008  |  0.903536243556  |  21.172347568997793
88  :  0.900830902446  |  0.89740005815  |  22.890916615000606
91  :  0.894450372015  |  0.903536243556  |  24.885566822998953
94  :  0.896413459641  |  0.899365496466  |  22.149469375999615
97  :  0.896413459641  |  0.89740005815  |  22.629668972997024
100  :  0.894372010908  |  0.899365496466  |  22.135012936003477
103  :  0.896413459641  |  0.899365496466  |  24.765393489000417
106  :  0.896413459641  |  0.899365496466  |  23.322617641999386
109  :  0.894450372015  |  0.899365496466  |  23.369004442000005

Dataset reading time: 0.36109152200151584
maximum_depth test...
1  :  0.861522495848  |  0.898933896201  |  2.5189442120026797
2  :  0.864607389004  |  0.92331526632  |  4.1253627379992395
3  :  0.871220407192  |  0.888733027014  |  5.4653686080018815
4  :  0.867548685845  |  0.919133726467  |  6.340844648999337
5  :  0.892768290236  |  0.914815366096  |  7.575491378000152
10  :  0.889076845355  |  0.892277285325  |  8.90408578700226
20  :  0.953600918812  |  0.886857824005  |  8.519998921001388
50  :  0.889932580818  |  0.886857824005  |  8.751030891999108
100  :  0.904579539528  |  0.886857824005  |  9.20137148899812


"""