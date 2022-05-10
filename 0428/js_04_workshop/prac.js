const user = {
    name:'박정현',
    age:18,
    balance:10000000000
}

function printUser ({name, age, balance}) {
    console.log(name, age, balance)
}

printUser(user)

// {name, age, balance} = user가 되기 때문에 name, age, user에 user.name, user.age, user.balance가 알아서 들어가게 됨


// this
// . 찍고 사용 가능하다? -> 메서드다? -> this는 methiod를 가리킴

const me = {
    name:'정현',
    age:20
}

function getFullName() {
    return this.name + this.age
}

// 1. 점 안찍고 썼네? 메서드로 쓰인게 아니네? getFullName의 this는 window를 가리키네?
getFullName()

// 2. 점 찍고 썼네? 메서드로 사용됐네? getFullName의 this는 앞의 me를 가리키네?
me.getFullName()