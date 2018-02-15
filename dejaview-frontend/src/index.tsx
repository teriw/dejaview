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



// const tick = () => {
    
//     const element = (
//         <div>
//             <h1>Hello, world</h1>
//             <h2>
//                 It is{' '}
//                 {new Date().toLocaleTimeString()}.
//             </h2>
//             <Welcome name="@benysimm" />
//         </div>
//     );

//     ReactDOM.render(
//         element,
//         document.getElementById('app')
//     );
// }

// setInterval(tick, 1000);




class Welcome extends React.Component<any, any> {
    constructor(props: any) {
        super(props);
    }

    


    componentDidMount() {
        var that = this;

        fetch('http://localhost:5000/api/scrapjob')
        .then(results => {
            // return results.json();
            return results.json();
        })
        .then(data => {
            let scrapjobs = data.map((scrapjob: any) => {

                console.log("dumping scrapjob", scrapjob);

                return(
                    <div>{scrapjob}</div>
                )
            })

            console.log("dumping scrapjobs", scrapjobs);

            that.setState({scrapjobs: scrapjobs});

            console.log("component did mount", that.state.scrapjobs);
        })

        
    }


    public render() {

        if (this.state == null) {
            return (
                <p>state is null</p>
            )
        }

        //return <h3>Hello, {this.props.name}</h3>;

        console.log("rendering!", this.state);
        // console.log("rendering!", this.state.scrapjobs);

        // const personLoc = Object.keys(this.state.person.loc).map((content, idx) => {
        //     const items = this.state.person.loc[content].map((item, i) => (
        //         <p key={i}>{item.text}</p>
        //     ))
        
        //     return <div key={idx}>{items}</div>
        // })

        // Object.keys(this.state.scrapjobs).map((content, idx) => {
        //     console.log("helloo?", content)

        // })

        // const items = this.state.

        // const items = this.state.scrapjobs.map((item: any, i: any) => (
        //     console.log("HAH", item)
        // ))

        return (
            <div className="container">
                {this.state.scrapjobs}
            </div>
        )
    }
    
}






class Assets extends React.Component<any, any> {
    constructor(props: any) {
        super(props);
    }

    componentDidMount() {
        var that = this;

        fetch('http://localhost:5000/api/scrapjob')
            .then(results => {
                // return results.json();
                return results.json();
            })
            .then(data => {
                let scrapjobs = data.map((scrapjob: any) => {

                    console.log("dumping scrapjob", scrapjob);

                    return (
                        <div>{scrapjob}</div>
                    )
                })

                console.log("dumping scrapjobs", scrapjobs);

                that.setState({ scrapjobs: scrapjobs });

                console.log("component did mount", that.state.scrapjobs);
            })


    }


    public render() {

        if (this.state == null) {
            return
        }

        //return <h3>Hello, {this.props.name}</h3>;

        console.log("rendering!", this.state);
        // console.log("rendering!", this.state.scrapjobs);

        // const personLoc = Object.keys(this.state.person.loc).map((content, idx) => {
        //     const items = this.state.person.loc[content].map((item, i) => (
        //         <p key={i}>{item.text}</p>
        //     ))

        //     return <div key={idx}>{items}</div>
        // })

        // Object.keys(this.state.scrapjobs).map((content, idx) => {
        //     console.log("helloo?", content)

        // })

        // const items = this.state.

        // const items = this.state.scrapjobs.map((item: any, i: any) => (
        //     console.log("HAH", item)
        // ))

        return (
            <div>
                <nav className="level">
                    <p className="level-item has-text-centered">
                        <figure className="image">
                        <img src={"./images/640x480.png"} />
                        </figure>
                    </p>
                    <p className="level-item">
                        <article className="media">
                            <div className="media-content">
                                <div className="field">
                                    <p className="control">
                                        <textarea className="textarea" placeholder="Add a comment..."></textarea>
                                    </p>
                                </div>
                                <nav className="level">
                                    <div className="level-left">
                                        <div className="level-item">
                                            <a className="button is-info">Submit</a>
                                        </div>
                                    </div>
                                </nav>
                            </div>
                        </article>
                    </p>
                </nav>
                <hr />
            </div>
        )
            
            
    }
    
}
