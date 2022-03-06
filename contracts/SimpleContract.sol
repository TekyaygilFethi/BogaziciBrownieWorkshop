//SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

struct Hero {
    string name;
    string lightsaberColor;
    uint16 age;
}

contract SimpleContract {
    Hero[] heroes;
    mapping(string => uint256) nameToIndex;

    function addHero(
        string memory name,
        string memory lightsaberColor,
        uint16 age
    ) public {
        heroes.push(Hero(name, lightsaberColor, age));
        uint256 idx = heroes.length - 1;
        nameToIndex[name] = idx;
    }

    function getAllHeroes() public view returns (Hero[] memory) {
        return heroes;
    }

    function getHeroByName(string memory name)
        public
        view
        returns (Hero memory)
    {
        uint256 idx = nameToIndex[name];
        return heroes[idx];
    }
}
