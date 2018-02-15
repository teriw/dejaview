using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;

namespace dejaview_api.Controllers
{
    [Route("api/[controller]")]
    public class AssetsController : Controller
    {
        // GET api/scrapjob
        // Returns a list of scrap jobs that need to be done.
        public IEnumerable<string> Get()
        {
            return new string[]
            {
                "4f817e9d3ad82887d8cac11f1c41e198", 
                "08d7baf2c4338914f8d10a85f28c2a67"
            };
        }

        // GET api/assets/20-Haines-Street-Curtin-ACT-2605
        [HttpGet("{id}")]
        public IEnumerable<Model.Asset> Get(string id)
        {
            return new List<Model.Asset>() {
                new Model.Asset() {
                    Id = "One",
                    BlobUri = "file:///home/ben/Pictures/640x480.png",
                    DateCreated = new DateTime(2018, 1, 28),
                    Source = "allhomes.com.au"
                },
                new Model.Asset() {
                    Id = "Two",
                    BlobUri = "file:///home/ben/Pictures/640x480.png",
                    DateCreated = new DateTime(2018, 1, 28),
                    Source = "allhomes.com.au"
                }
            };
        }

        // POST api/values
        [HttpPost]
        public void Post([FromBody]string value)
        {
        }

        // PUT api/values/5
        [HttpPut("{id}")]
        public void Put(int id, [FromBody]string value)
        {
        }

        // DELETE api/values/5
        [HttpDelete("{id}")]
        public void Delete(int id)
        {
        }
    }
}
