import React from 'react';
import ReactDOM from 'react-dom';



let x = 0;
const PI = 3.141593;

let nums: number[] = [2, 3, 5, 7, 8, 9, 10, 11, 12];
let fives: number[] = [];

nums.forEach((v, i) => {
    if (v % 5 === 0) {
        fives.push(v);
        console.log("ping ping ${v}");
    }
});



class Shape {
    foo: string;

    constructor(id: string, x: number, y: number) {
        console.log('poo');
        let b = id + y + x;
        this.foo = "";
    }
};



// const App = () => {
//     return (
//         <div>
//             <h1>hello worlds</h1>
//         </div>
//     )
// }

// ReactDOM.render(
//     <App />,
//     document.getElementById('app')
// );



const tick = () => {
    
    const element = (
        <div>
            <h1>Hello, world</h1>
            <h2>
                It is{' '}
                {new Date().toLocaleTimeString()}.
            </h2>
            <Welcome name="@benysimm" />
        </div>
    );

    ReactDOM.render(
        element,
        document.getElementById('app')
    );
}

setInterval(tick, 1000);




class Welcome extends React.Component<any, any> {
    constructor(props: any) {
        super(props);
    }

    public render() {
        return <h3>Hello, {this.props.name}</h3>;
    }
}
