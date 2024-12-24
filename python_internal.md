```mermaid
graph TD
    score --> Value_10["10"]
    a_score --> Value_10
    Value_10 --> ref_count_10["ref_count: 2"]
    a --> Value_5["5"]
    b --> Value_2["2"]
    Value_5 --> ref_count_5["ref_count: 1"]
    Value_2 --> ref_count_2["ref_count: 1"]
    a --> Value_7["7"]
    Value_7 --> ref_count_7["ref_count: 1"]
    
    
 