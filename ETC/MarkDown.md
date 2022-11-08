# MarkDown
    Explanation MarkDown for Github



# 목차
[1. Headers 헤더](#1-headers-헤더)    
[2. Emphasis 강조](#2-emphasis-강조)    
[3. Blockquotes 인용](#3-blockquotes-인용)    
[4. Lists 목록](#4-lists-목록)      
[5. Backslash Escapes 백슬래쉬 이스케이프](#5-backslash-escapes-백슬래쉬-이스케이프)  
[6. Images 이미지](#6-images-이미지)  
[7. Links 링크](#7-links-링크)  
[8. Fenced Code Blocks 코드 블럭](#8-fenced-code-blocks-코드-블럭)  
[9. Task Lisk 체크 리스트](#9-task-lisk-체크-리스트)  
[10. Horizontal Rules 수평선](#10-horizontal-rules-수평선)  
[11. Emoji 이모티콘](#11-emoji-이모티콘)  
[12. Table 테이블](#12-table-테이블)  
[13. Line Breaks 줄바꿈](#13-line-breaks-줄바꿈)  



## 1. Headers 헤더
 *   #으로 시작하는 텍스트.
 *  #은 하나부터 여섯개까지 가능.
 *  #이 늘어날때마다 제목의 스케일 낮아집니다.
 *  H1은 ===로도 만들 수 있습니다.
 *  H2는 ---로도 만들 수 있습니다.

## Syntax 마크다운 사용법
```
This is an H1
===
This is an H2
---
# This is an H1
## This is an H2
### This is an H3
#### This is an H4
##### This is an H5
###### This is an H6   
```

## 2. Emphasis 강조
* 기울여 쓰기(italic) : * 또는 _로 감싼 텍스트.
* 두껍게 쓰기(bold) : ** 또는 __로 감싼 텍스트.
* 취소선 : ~~로 감싼 텍스트.
* 이탤릭체와 두껍게를 같이 사용할 수 있습니다.
```
  *This text will be italic*
  _This will also be italic_
  **This text will be bold**
  __This will also be bold__
  ~~This is canceled~~
  *You **can** combine them*

```
## 3. Blockquotes 인용
* >으로 시작하는 텍스트.
* >는 3개까지 가능합니다.
* 1개는 인용문.
* 2개는 인용문 안에 인용문.
* 3개는 인용문 안에 인용문 안에 인용문.

```
As Grace Hopper said:
> I’ve always been more interested in the future than in the past.    
> This is a first blockquote.
> > This is a second blockquote.
> > > This is a third blockquote.
```

### Demonstration 실행결과  
As Grace Hopper said:       
> I’ve always been more interested in the future than in the past.          
> This is a first blockquote.       
> > This is a second blockquote.        
> > > This is a third blockquote.       

## 4. Lists 목록
### 4.1. Unordered lists 순서가 없는 목록  

* *, +, - 를 이용해서 순서가 없는 목록을 만들 수 있습니다.
* 들여쓰기를 하면 모양이 바뀝니다.
### 4.2. Ordered lists 순서가 있는 목록  

* 숫자를 기입하면 순서가 있는 목록이 됩니다.
* 들여쓰기를 하면 모양이 바뀝니다.

```
* Item 1
* Item 2
  * Item 1
  * Item 2
    * Item 1
    * Item 2
 1. Item 1
 2. Item 2
 3. Item 3
   1. Item 1
   2. Item 2
   3. Item 3
     1. Item 1
     2. Item 2
     3. Item 3
```




## 5. Backslash Escapes 백슬래쉬 이스케이프
* 특수문자를 표현할 때, 표시될 문자 앞에 \를 넣고 특수문자를 쓰면 됩니다.
* 주의할 점은 앞과 뒤에가 형식이 똑같이 백슬래쉬 뒤에 특수문자입니다. 감싸는 형태가 아닙니다.
* 백슬래쉬는 아래의 특수문자를 표현할 수 있습니다.
* \ backslash, \ backtick, * asterisk, _ underscore, {} curly braces, [] square brackets, () parentheses, # hash mark, + plus sign, - minus sign (hyphen), . dot, ! exclamation mark

### Syntax 마크다운 사용법
```
\*literal asterisks\*
\#hash mark\#
\[squre brackets\]
```
## Demonstration 실행결과

*literal asterisks*  
#hash mark#  
[squre brackets]


## 6. Images 이미지
* 사진 깃 허브 안으로 드래그
* 이미지의 사이즈를 변경하기 위해서는 <img width="OOOpx" height="OOOpx"> 링크 </img>와 같이 표현합니다.
* 

![tomato](https://user-images.githubusercontent.com/75108382/184267939-040f6114-35c4-4d68-9e23-7ccecd7a1dd2.jpg)



## 7. Links 링크
## 7.1. External Links 외부 링크
```
인라인 링크: [링크](http://example.com "링크 제목")
url 링크: <example.com>, <example@example.com>; 꺽쇠 괄호 없어도 자동으로 링크를 사용
```
```
[Google](http://www.google.com "구글")
[Naver](http://www.naver.com "네이버")
[Github](http://www.github.com "깃허브")
구글 www.google.com; 꺽쇠없음
네이버 <www.naver.com>; 꺽쇠있음
My mail <jinkyukim.dev@gmail.com>
```
### Demonstration 실행결과
Google  
Naver  
Github  
구글 www.google.com  
네이버 <www.naver.com>  
My mail jinkyukim.dev@gmail.com  


## 8. Fenced Code Blocks 코드 블럭
* 간단한 인라인 코드는 텍스트를 앞뒤로 `기호로 감싸면 됩니다.
*  ` `` 혹은 ~~~ 코드.
* 첫 줄과 마지막 줄에 Back quote ( ` ) 또는 물결( ~ ) 3개 삽입.
* 코드가 여러 줄인 경우, 줄 앞에 공백 네 칸을 추가하면 됩니다.
*  ` `` 옆에 언어를 지정해주면 syntax color가 적용됩니다.


## 9. Task Lisk 체크 리스트

* 줄 앞에 - [x]를 써서 완료된 리스트 표시.
* 줄 앞에 - [ ]를 써서 미완료된 리스트 표시.
* 체크 안에서 강조 외에 여러 기능을 사용할 수 있습니다.

## Syntax 마크다운 사용법
```
- [x] this is a complete item
- [ ] this is an incomplete item
- [x] @mentions, #refs, [links](),
**formatting**, and <del>tags</del>
supported
- [x] list syntax required (any
unordered or ordered list
supported)
```

### Demonstration 실행결과
- [x] this is a complete item
- [ ] this is an incomplete item
- [x] @mentions, #refs, [links](),
**formatting**, and <del>tags</del>
supported
- [x] list syntax required (any
unordered or ordered list
supported)

## 10. Horizontal Rules 수평선
* - 또는 * 또는 _ 을 3개 이상 작성.
* 단, -을 사용할 경우 header로 인식할 수 있으니 이 전 라인은 비워두어야 합니다.

```
* * *
***
*****
- - -
-------------------
```

### Demonstration 실행결과
* * *
***
*****
- - -
-------------------


## 11. Emoji 이모티콘
* 마크다운을 이용해 이모티콘을 표현가능.
* 깃허브도 적용가능.
* 더 많은 리스트는 아래의 사이트로 방문.
* www.emoji-cheat-sheet.com
```
GitHub supports emoji!
:+1: :sparkles: :camel: :tada:
:rocket: :metal: :octocat:
```
### Demonstration 실행결과
GitHub supports emoji!
:+1: :sparkles: :camel: :tada:
:rocket: :metal: :octocat:

## 12. Table 테이블
* 헤더와 셀을 구분할 때 3개 이상의 -(hyphen/dash) 기호가 필요합니다.
* 헤더 셀을 구분하면서 :(Colons) 기호로 셀(열/칸) 안에 내용을 정렬할 수 있습니다.
* 가장 좌측과 가장 우측에 있는 |(vertical bar) 기호는 생략 가능합니다.
```
테이블 생성

헤더1|헤더2|헤더3|헤더4
---|---|---|---
셀1|셀2|셀3|셀4
셀5|셀6|셀7|셀8
셀9|셀10|셀11|셀12

테이블 정렬

헤더1|헤더2|헤더3
:---|:---:|---:
Left|Center|Right
1|2|3
4|5|6
7|8|9
```

### Demonstration 실행결과
테이블 생성

헤더1|헤더2|헤더3|헤더4
---|---|---|---
셀1|셀2|셀3|셀4
셀5|셀6|셀7|셀8
셀9|셀10|셀11|셀12

테이블 정렬

헤더1|헤더2|헤더3
:---|:---:|---:
Left|Center|Right
1|2|3
4|5|6
7|8|9


## 13. Line Breaks 줄바꿈
* ```<br>```를 활용해서 줄바꿈을 할 수 있습니다.
* 맨 뒤에서 뛰어쓰기 2번도 가능
