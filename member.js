function skillsMember() {
    var member = {
        name: 'John Doe',
        skills: ['JavaScript', 'React', 'Node.js'],
        showSkills: function () {
            this.skills.forEach(function (skill) {
                console.log(`${this.name} knows ${skill}`);
            });
        }
    };
    member.showSkills();
}