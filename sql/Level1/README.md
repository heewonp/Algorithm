# Level 1에서 나온 SQL 문법 정리

> select 문을 사용해 테이블의 데이터를 선택할 수 있다.
>
> ```mysql
> select 필드이름
> from 테이블이름
> ```
>
> 기본 구조

1. 모든 데이터를 전부 가져오고 싶을 경우

 ``` mysql
select * from 테이블명 
-- * 을 붙여주면 테이블의 모든 컬럼을 가져올 수 있다.
 ```

2. 데이터 정렬 `order by`

```mysql
select * from 테이블명 order by 정렬할 컬럼 asc
-- asc : 오름 차순 (생략 가능)
-- desc: 내림 차순
```

3. 조건에 맞는 데이터를 찾기

```mysql
select * from 테이블명 where 조건 (컬럼명 = 찾을 내용 )
select * from 테이블명 where 조건 and(or)조건
```

4. NOT IN

```mysql
select * from 테이블명 where 컬럼명 NOT IN ('포함되지 않을 내용')
-- 특정 컬럼 데이터중 포함하고 싶지 않은 내용을 보여줄때
```

5. LIMIT(MySQL)

```mysql
-- 출력 데이터의 개수를 제한할 때 사용한다.
select * from 테이블명 LIMIT 3
-- 3번째 까지만 가져오겠다.
select * from 테이블명 1,5
-- 2번째 부터 5개 출력
```

6. LIMIT를 Oracle에서 사용하고 싶을 경우

```sql
select *
from(
	select *
	from 테이블명
	)
where rownum = 3
-- 3번째 까지만 가져오겠다.

select *
from(
	select *
	from 테이블명
	)
where rownum >=3 and rownum<=5
-- 2번째 부터 5개 출력
```

