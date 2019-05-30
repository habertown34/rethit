pragma solidity = 0.5.9;

contract Rethit {

    uint public latestPostID;

    struct Post
    {
        uint postID;
        address poster;
        string content;
        int votes;
    }

    mapping (uint => Post) public posts;

    constructor() public {
        latestPostID = 0;
    }

    function create(string memory _content) public {
        latestPostID++;
        Post memory p = Post(latestPostID, msg.sender, _content, 0);
        posts[latestPostID] = p;
    }

    function upvote(uint id) public
    {
        posts[id].votes++;
    }

    function downvote(uint id) public
    {
        posts[id].votes--;
    }

    function test() public pure returns (string memory) 
    {
        return 'Hello world';
    }
}