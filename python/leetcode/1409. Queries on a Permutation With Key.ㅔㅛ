class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        
        m_list = [i for i in range(1,m+1)]
        
        for i,x in enumerate(queries):
            
            p = m_list.index(x)
            
            queries[i] = p
            
            m_list.pop(p)
            
            m_list.insert(0,x)
            
        return queries