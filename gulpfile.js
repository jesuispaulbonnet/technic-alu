// Include gulp
var gulp = require('gulp');
var sass = require('gulp-sass');
var rename = require('gulp-rename');


// Compile Our Sass
gulp.task('sass', function() {
    return gulp.src('technic_alu/static/sass/technic_alu.scss')
        .pipe(sass({outputStyle: 'compressed'}))
        .pipe(rename('technic_alu.min.css'))
        .pipe(gulp.dest('technic_alu/static/css'));
});
