SELECT outs.ANIMAL_ID, outs.name from ANIMAL_OUTS as outs  
left join ANIMAL_INS  as ins on ins.ANIMAL_ID = outs.ANIMAL_ID
where ins.ANIMAL_ID is null
order by outs.ANIMAL_ID asc