# python-designPattern
单一职责 	具体例子:组件化,修改某个组件不会影响到其他组件和业务降低耦合度,引入简单方便

开放封闭原则	对扩展开放 对修改封闭, 每当功能变化的时候 都要对变化和预判进行抽象,使得将来新增功能的时候,只要新增代码而不需要修改旧代码

依赖到转原则	面向接口编程,依赖抽象(接口)不要依赖细节(具体类)

迪米特法则    两个类不要相互依赖,而是通过第三个类去调用对方 (适配器模式)



python设计模式 

以下是 工程中对应的目录

1.工厂方法和抽象工厂    factory

2.原型模式  prototypePattern

3.代理模式 proxyPattern

4.观察者模式  observerPattern

5.单例模式(double check 线程安全) singleton

6.装饰模式	decoratorPattern

7.状态模式	statePattern

8.建造者模式  buiderPattern

9.适配器模式  adapterPattern

10.模板模式  没写,例子:从androidStudio 新建activity ,activity已经把具体的生命周期做好,我们只需要在oncreate 等方法中做填空题

11.外观模式 没写,例子:复杂服务端接口的网关

12.享元模式 没写,例子:java的String类

13.策略模式 没写 太熟悉了 例子 我的开源项目kotlinArch的分页规则封装,将计算规则抽象出来,用接口表示,使得具体计算方法,可以用被封装成一个个策略类,通过替换策略,来替换不同的规则,还有一个经典的用法:通过 工厂模式+策略模式,去除业务中的大量if判断

