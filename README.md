# python-designPattern


**我并不非常熟悉python,之所以用python不用java是因为我想证明我是掌握了思想,而不局限任何语言,也不是背了代码**





* 单一职责 	具体例子:组件化,修改某个组件不会影响到其他组件和业务降低耦合度,引入简单方便

* 开放封闭原则	对扩展开放 对修改封闭, 每当功能变化的时候 都要对变化和预判进行抽象,使得将来新增功能的时候,只要新增代码而不需要修改旧代码

* 依赖到转原则	面向接口编程,依赖抽象(接口)不要依赖细节(具体类)

* 迪米特法则    两个类不要相互依赖,而是通过第三个类去调用对方 (适配器模式)




**以下是 工程中对应的目录**

* 1.工厂方法和抽象工厂    factory
* 2.原型模式  prototypePattern
* 3.代理模式 proxyPattern
* 4.观察者模式  observerPattern
* 5.单例模式(double check 线程安全) singleton
* 6.装饰模式	decoratorPattern
* 7.状态模式	statePattern
* 8.建造者模式  buiderPattern
* 9.适配器模式  adapterPattern
* 10.模板模式  没写,例子:从androidStudio 新建activity ,activity已经把具体的生命周期做好,我们只需要在oncreate 等方法中做填空题
* 11.外观模式 没写,例子:复杂服务端接口的网关
* 12.享元模式 没写,例子:java的String类
* 13.策略模式 没写 太熟悉了 例子 我的开源项目kotlinArch的分页规则封装,将计算规则抽象出来,用接口表示,使得具体计算方法,可以用被封装成一个个策略类,通过替换策略,来替换不同的规则,还有一个经典的用法:通过 工厂模式+策略模式,去除业务中的大量if判断
* 14.备忘录模式   memoPattern
* 15.组合模式 没写,就是一种树形数据结构
* 16.迭代器模式  iteratorPattern         设计一个迭代器 为集合 提供 has_next() 和 next()方法 进行遍历  
* 17.桥接模式 bridgePattern, 桥接模式是将 A继承B B继承C 这种形式拆分成 B继承C  B持有A的形式,举个例子 将多重继承拆分开,并保持两个父类的特性
* 18.命令模式 commandPattern 命令模式 是通过命令 将 boss和员工 分隔开,不让boss直接调用员工,根据敏捷开发原则,没啥事可以不用特地使用命令模式
* 19.责任链模式responsePattern
* 20.中介者模式 mediatorPattern 房东和买家通过中介 进行沟通, 中介依赖 两个people(房东和买家), 房东和买家各自依赖中介,people要相互沟通,要调用中介的方法,通过中介来执行

**to be continued,老夫将持续更新**

