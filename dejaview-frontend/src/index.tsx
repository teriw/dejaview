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
        console.log('superman');
        let b = id + y + x;
        this.foo = "";
    }
};




class Assets extends React.Component<any, any> {

    timerID: any;

    constructor(props: any) {
        super(props);
    }

    componentDidMount() {
        this.timerID = setInterval(
            () => this.tick(),
            5000
          );
    }


    componentWillUnmount() {
        clearInterval(this.timerID);
      }
    


    tick() {
        var that = this;
        
        fetch('http://localhost:5000/api/assets/20-haines-st-curtin-act-2605')
            .then(results => {
                return results.json();
            })
            .then(data => {
                let assets = data.map((asset: any) => {

                    console.log("dumping asset", asset);

                    return (
                        <div>
                            <h1>{asset.id}</h1>
                            <nav className="level">
                                <p className="level-item has-text-centered">
                                    <figure className="image">
                                        <img src={asset.blobUri} />
                                    </figure>
                                </p>
                                <p className="">
                                    <article className="media">
                                        <div className="media-content">
                                            <div className="field">
                                                <p className="control">
                                                    <textarea className="textarea" placeholder="Add a comment..."></textarea>
                                                </p>
                                            </div>
                                            
                                            <a className="button is-info">Submit</a>
                                        </div>
                                    </article>
                                    <div className="field is-grouped is-grouped-multiline margin-top-20">
                                        <div className="control">
                                            <div className="tags has-addons">
                                            <span className="tag is-dark">date</span>
                                            <span className="tag is-info">Hours ago</span>
                                            </div>
                                        </div>

                                        <div className="control">
                                            <div className="tags has-addons">
                                            <span className="tag is-dark">source</span>
                                            <span className="tag is-success">{asset.source}</span>
                                            </div>
                                        </div>
                                    </div>
                                </p>
                            </nav>

                            

                            <hr />
                        </div>
                    )
                })

                console.log("dumping assets", assets);

                that.setState({ assets: assets });

                console.log("component did mount", that.state.scrapjobs);
            })
    }


    public render() {

        if (this.state == null) {
            return (
                <div></div>
            )
        }
        console.log("rendering!", this.state);

        return (
            <div>
                {this.state.assets}
            </div>
        )
    }
    
}




ReactDOM.render(
    <Assets />,
    document.getElementById('app')
);